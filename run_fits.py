#!/usr/bin/env python
import os
import sys
from read_config import read_config

def run_fits(configuration):
    """
    runs therm2_hbtfit for femtopipi*.root files
    hbtfit*.ini are copied as hbtfit.ini file 
    to dirs where femtopipi*.root are located
    dependently on kt range: 
        for kt  = 1a (0.2-0.3) hbtfit_maxfitrange02.ini is copied
        for kt != 1a           hbtfit_maxfitrange03.ini is copied
    """

    def copy_init():
        """
        copies content of hbtfit.ini to hbtfit_maxfitrange[02/03].ini
        besides MaxFitRange parameter and RejectRange
        """
        with open(configuration['hbtfit_ini_file']) as ini:
            with open(configuration['hbtfit_ini_file']+'_maxfitrange02','w') as ini02, \
                 open(configuration['hbtfit_ini_file']+'_maxfitrange03', 'w') as ini03:
                    for line in ini:
                        if line.startswith('MaxFitRange'):
                            max_fit_range = configuration['max_fit_range'].replace('0','0.',1)
                            ini02.write('MaxFitRange = 0.2\n')
                            ini03.write('MaxFitRange = '+ max_fit_range +'\n')
                        elif line.startswith('RejectRange ='):
                            reject = configuration['rejection'].replace('00','0.0')
                            RR = 'RejectRange = '+reject+'\n'
                            ini02.write(RR)
                            ini03.write(RR)
                        else: 
                            ini02.write(line)
                            ini03.write(line)


    kt_lst = ['1a', '2a', '3a', '4a', '5a', '6a']
    #rapid_lst = ['m2515', 'm1505','m1zero', 'm0505', 'p0515', 'p1525']
    rapid_lst = ['m1zero',
                 'm25m2', 'm2m15', 'm15m1', 'm1m05', 'm05m0', 
                 'p0p05', 'p05p1', 'p1p15', 'p15p2', 'p2p25'] 
    #rapid_lst = ['m1zero',]


    fit_input_dir = configuration['fit_input_dir']
    reject_func = configuration['reject_func'] 

    copy_init()

    for dir in [fit_input_dir+y+'/' for y in rapid_lst]:
        if not os.path.exists(dir): continue
        with open(dir+'hbtradii.txt', 'w') as _: pass # make it empty
        for kt in kt_lst:
            file = 'femtopipi'+kt+'.root'
            if not os.path.exists(dir+file): continue
            print '\npy: running fit for '+dir+file+'\tkt='+kt

            if kt == '1a': 
                os.system('cp '+configuration['hbtfit_ini_file']+'_maxfitrange02'+' hbtfit.ini')
                #print 'py: kt={} => coping hbtfit_maxfitrange02.ini to hbtfit.ini'.format(kt)
            else:
                os.system('cp '+configuration['hbtfit_ini_file']+'_maxfitrange03'+' hbtfit.ini')
                #print 'py: kt={} => coping hbtfit_maxfitrange03.ini to hbtfit.ini'.format(kt)
            command = 'therm2/therm2_hbtfit_'+reject_func+' '+dir+file+' 2>/dev/null'
            print command
            os.system(command)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if __name__ == '__main__':
    if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
    else: configuration = read_config()
    run_fits(configuration)
