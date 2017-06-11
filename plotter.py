#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from read_config import read_config


# parsing argvs
if len(sys.argv) > 3: configuration = read_config(sys.argv[3])
else: configuration = read_config()
fit_input_dir = configuration['fit_input_dir']
fit_output_dir = configuration['fit_output_dir']
atlas_data_dir = configuration['atlas_data_dir'] 

datafile, figfile = sys.argv[1:3]
if not datafile.startswith(fit_output_dir ): datafile = fit_output_dir + datafile
if not datafile.endswith('.dat'): datafile = datafile+'.dat'

outfile = fit_output_dir +'fig_'+figfile+'.png'
figfile = atlas_data_dir +'fig_'+figfile+'.dat'


kt_dict = {'1a':(0.2,0.3),'2a':(0.3,0.4),'3a':(0.4,0.5),'4a':(0.5,0.6),'5a':(0.6,0.7),'6a':(0.7,0.8)}
rapid_dict = {'m2515':(-2.5,-1.5), 'm1505':(-1.5, -0.5),'m1zero':(-1., 0.0), 'm0505':(-0.5, 0.5), 'p0515':(0.5,1.5), 'p1525':(1.5,2.5)}


atlasx, atlasy = [],[]
with open(figfile) as data:
    for line in data:
        if len(line.split())<2: continue 
        atlasx.append(float(line.split()[0])) 
        atlasy.append(float(line.split()[1])) 

fig,ax = plt.subplots()
ax.plot(atlasx,atlasy,'ro-', label='ATLAS')

x, xerror, y, yerror = [],[],[],[]
with open(datafile) as data:
    if '_p' in datafile or '_m' in datafile:
        # case for set rapid, xaxis = kt
        for line in data:
            x1,x2 = kt_dict[line.split()[0]]
            x1,x2 = float(x1), float(x2)
            x.append((x1+x2)/2)
            xerror.append((x2-x1)/2.)
            y.append(float(line.split()[1]))
            yerror.append(float(line.split()[3]))
            ax.set_xlabel('kt', fontsize=20)
    elif 'a.dat' in datafile:
        # case for set kt, xaxis = rapid
        for line in data:
            #if line.split()[0] == 'm1zero': continue
            x1,x2 = rapid_dict[line.split()[0]]
            x1,x2 = float(x1), float(x2)
            x.append((x1+x2)/2)
            xerror.append((x2-x1)/2.)
            y.append(float(line.split()[1]))
            yerror.append(float(line.split()[3]))
            ax.set_xlabel('y', fontsize=20)
    else: print '\n\n\t\tWARNING: cannot find out as a func of WHAT to plot, neither \'a.dat\' nor \'_p/m\' in filename\n\n'

if 'lambda' in datafile: ax.set_ylabel('$\lambda$', fontsize=20)
else: ax.set_ylabel('$'+datafile.split('/')[-1].split('_')[-2].replace('r', 'R_{')+'}$', fontsize=20)

ax.text(0.7, 0.05, 'source:\n'+datafile, transform=ax.transAxes)
ax.errorbar(x,y,xerr=xerror,yerr=yerror,fmt='bo-', label='therm')
ax.legend()
ax.grid(True)
#plt.show()        
plt.savefig(outfile)
