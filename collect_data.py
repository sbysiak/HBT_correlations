#!/usr/bin/env python
import os
import sys
from read_config import read_config

var_lst = ['lambda', 'rout', 'rside', 'rlong', 'routlong']
kt_lst = ['1a', '2a', '3a', '4a', '5a', '6a']
rapid_lst = ['m2515', 'm1505','m1zero', 'm0505', 'p0515', 'p1525']

def parse(datafile):
    with open(datafile) as data:
        for line in data:
            if '.root' in line:
                tmp=line.split(']')[1]
                rapid = tmp.split('/')[-2].strip()
                kt = tmp.split('/')[-1].replace('.root', '').replace('femtopipi','').strip()
                print 'rapid, kt: ', rapid, kt
            elif '+/-' in line:
                var = line.split()[0].lower() # var=lambda,rout ...
                mean = line.split()[1] 
                std = line.split()[3]
                with open(fit_output_dir+var+'_'+rapid+'.dat','a') as outfile:
                    outfile.write(kt+' '+mean+' +/- '+std+'\n')
                with open(fit_output_dir+var+'_'+kt+'.dat','a') as outfile:
                    outfile.write(rapid+' '+mean+' +/- '+std+'\n')

if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
else: configuration = read_config()
fit_input_dir = configuration['fit_input_dir']
fit_output_dir = configuration['fit_output_dir']

if not os.path.exists(fit_output_dir): 
    print 'creating fit_output_dir \'{}\''.format(fit_output_dir)
    os.system('mkdir '+fit_output_dir)

# make files empty if exist
for var in var_lst:
    for kt in kt_lst:
        f=open(fit_output_dir+var+'_'+kt+'.dat', 'w')
        f.close()
    for y in rapid_lst:
        f=open(fit_output_dir+var+'_'+y+'.dat', 'w')
        f.close()

for dir in [y for y in rapid_lst]:
    dir = fit_input_dir+dir+'/'
    if not os.path.exists(dir): continue

    file = 'hbtradii.txt'
    parse(dir+file)
