#!/usr/bin/env python
import os
import sys
from read_config import read_config


def collect_data(configuration):
    """
    hbtradii.txt contains all fit parameters (e.g. R_out, R_side) values 
    for particular kt and rapidity
    function searches for all values of selected parameter and kt OR rapidity
    and writes them to files < parameter_name >_< kt/rapidity >
    """

    var_lst = ['lambda', 'rout', 'rside', 'rlong', 'routlong']
    kt_lst = ['1a', '2a', '3a', '4a', '5a', '6a']
    #rapid_lst = ['m2515', 'm1505','m1zero', 'm0505', 'p0515', 'p1525']  // old division
    rapid_lst = ['m25m2', 'm2m15', 'm15m1', 'm1m05', 'm05m0', 
                 'p0p05', 'p05p1', 'p1p15', 'p15p2', 'p2p25',  
                 'm1zero'] 


    def parse(datafile):
        with open(datafile) as data:
            for line in data:
                if '.root' in line:
                    # headers
                    tmp=line.split(']')[1]
                    rapid = tmp.split('/')[-2].strip()
                    kt = tmp.split('/')[-1].replace('.root', '').replace('femtopipi','').strip()
                    print 'rapid, kt: ', rapid, kt
                elif '+/-' in line:
                    # lines with numerical values
                    var = line.split()[0].lower() # var=lambda,rout ...
                    mean = line.split()[1] 
                    std = line.split()[3]
                    with open(fit_output_dir+var+'_'+rapid+'.dat','a') as outfile:
                        outfile.write(kt+' '+mean+' +/- '+std+'\n')
                    with open(fit_output_dir+var+'_'+kt+'.dat','a') as outfile:
                        outfile.write(rapid+' '+mean+' +/- '+std+'\n')

    fit_input_dir = configuration['fit_input_dir']
    fit_output_dir = configuration['fit_output_dir']
    centrality = configuration['centrality']

    if not os.path.exists('cent'+centrality): 
        print 'creating dir \'{}\''.format('cent'+centrality)
        os.system('mkdir cent'+centrality)

    if not os.path.exists(fit_output_dir): 
        print 'creating fit_output_dir \'{}\''.format(fit_output_dir)
        os.system('mkdir '+fit_output_dir)

    # make files empty if exist
    for var in var_lst:
        for kt in kt_lst:
            with open(fit_output_dir+var+'_'+kt+'.dat', 'w') as _: pass
        for y in rapid_lst:
            with open(fit_output_dir+var+'_'+y+'.dat', 'w') as _: pass
    
    for dir in [y for y in rapid_lst]:
        dir = fit_input_dir+dir+'/'
        if not os.path.exists(dir): continue

        file = 'hbtradii.txt'
        parse(dir+file)
# # # # # # # # # # # # # # # # # #


if __name__ == '__main__':
    if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
    else: configuration = read_config()
    collect_data(configuration)


