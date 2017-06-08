import os
import sys
from read_config import read_config

kt_lst = ['1a', '2a', '3a', '4a', '5a', '6a']
rapid_lst = ['m2515', 'm1505','m1zero', 'm0505', 'p0515', 'p1525']

# fit_input_dir = dir containing root files which are input for therm2_hbtfit

if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
else: configuration = read_config()
fit_input_dir = configuration['fit_input_dir']
fit_output_dir = configuration['fit_output_dir']


for dir in [fit_input_dir+y+'/' for y in rapid_lst]:
    if not os.path.exists(dir): continue
    os.system('cp hbtfit.ini '+dir)
    for file in ['femtopipi'+kt+'.root' for kt in kt_lst]:
        if not os.path.exists(dir+file): continue
        print 'py: '+dir+file+'\n'

        if kt == '1a': os.system('cp hbtfit_maxfitrange02.ini hbtfit.ini')
        os.system('therm2/therm2_hbtfit '+dir+file+' 2>/dev/null')
        if kt == '1a': os.system('cp hbtfit_maxfitrange03.ini hbtfit.ini')
