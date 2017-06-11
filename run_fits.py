#!/usr/bin/env python
import os
import sys
from read_config import read_config


def copy_init():
    with open('hbtfit.ini') as ini:
        with open('hbtfit_maxfitrange02.ini','w') as ini02:
            with open('hbtfit_maxfitrange03.ini', 'w') as ini03:
				for line in ini:
				    if line.startswith('MaxFitRange'):
				        ini02.write('MaxFitRange = 0.2')
				        ini03.write('MaxFitRange = 0.3')
				    else: 
				        ini02.write(line)
				        ini03.write(line)



kt_lst = ['1a', '2a', '3a', '4a', '5a', '6a']
rapid_lst = ['m2515', 'm1505','m1zero', 'm0505', 'p0515', 'p1525']

if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
else: configuration = read_config()
fit_input_dir = configuration['fit_input_dir']

copy_init()

for dir in [fit_input_dir+y+'/' for y in rapid_lst]:
    if not os.path.exists(dir): continue
    with open(dir+'hbtradii.txt', 'w') as _: pass # make it empty
    for kt in kt_lst:
        file = 'femtopipi'+kt+'.root'
        if not os.path.exists(dir+file): continue
        #print 'py: '+dir+file+'\tkt='+kt+'\n'

        if kt == '1a': 
            os.system('cp hbtfit_maxfitrange02.ini '+'hbtfit.ini')
            #print 'py: kt={} => coping hbtfit_maxfitrange02.ini to hbtfit.ini'.format(kt)
        else:
            os.system('cp hbtfit_maxfitrange03.ini '+'hbtfit.ini')
            #print 'py: kt={} => coping hbtfit_maxfitrange03.ini to hbtfit.ini'.format(kt)

        os.system('therm2/therm2_hbtfit '+dir+file+' 2>/dev/null')
