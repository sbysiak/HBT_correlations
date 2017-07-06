#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from read_config import read_config



def plot(configuration, datafile, figfile):
    fit_input_dir = configuration['fit_input_dir']
    fit_output_dir = configuration['fit_output_dir']
    atlas_data_dir = configuration['atlas_data_dir'] 
    centrality = configuration['centrality'] 
    rejection = configuration['rejection'] 


    if not datafile.startswith(fit_output_dir ): datafile = fit_output_dir + datafile
    if not datafile.endswith('.dat'): datafile = datafile+'.dat'

    outfile = fit_output_dir +'fig_'+figfile+'.png'
    figfile = atlas_data_dir +'fig_'+figfile+'_cent'+centrality+'.dat'


    kt_dict = {'1a':(0.2,0.3),
               '2a':(0.3,0.4),
               '3a':(0.4,0.5),
               '4a':(0.5,0.6),
               '5a':(0.6,0.7),
               '6a':(0.7,0.8)}
    rapid_dict = {'m2515':(-2.5,-1.5), 
                  'm1505':(-1.5, -0.5),
                  'm1zero':(-1., 0.0), 
                  'm0505':(-0.5, 0.5), 
                  'p0515':(0.5,1.5), 
                  'p1525':(1.5,2.5)}


    atlasx, atlasy = [],[]
    test_with_errors = False
    with open(figfile) as data:
        for line in data:
            if 'upper left' in line or 'lower right' in line: 
                test_with_errors = True
            if line.startswith('#'): continue
            if len(line.split())<2: continue 
            atlasx.append(float(line.split()[0])) 
            atlasy.append(float(line.split()[1]))


    fig,ax = plt.subplots()
    if test_with_errors:
        N = len(atlasx)/3
        atlasx_points = np.array(atlasx[:N])
        atlasx_left = atlasx_points - np.array(atlasx[N:2*N])
        atlasx_right = np.array(atlasx[2*N:3*N]) - atlasx_points
        atlasy_points = np.array(atlasy[:N])
        atlasy_upper = atlasy_points - np.array(atlasy[N:2*N])
        atlasy_lower = np.array(atlasy[2*N:3*N]) - atlasy_points

        ax.errorbar(atlasx_points,atlasy_points,
                    xerr=[atlasx_left, atlasx_right],
                    yerr=[atlasy_upper, atlasy_lower],
                    fmt='ro-', label='ATLAS')
    else:
        ax.plot(atlasx,atlasy,'ro-', label='ATLAS')



    x, xerror, y, yerror = [],[],[],[]
    with open(datafile) as data:
        if '_p' in datafile or '_m' in datafile:
            # case for set rapid, xaxis = kt
            for line in data:
                if line.startswith('#'): continue
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
                if line.startswith('#'): continue
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

    ax.text(0.98,0.02,'source:\n'+datafile, 
            horizontalalignment='right',
            verticalalignment='bottom',
            transform=ax.transAxes)
    #print 'length x,xerror,y,yerror', len(x), len(xerror), len(y), len(yerror)
    ax.errorbar(x,y,xerr=xerror,yerr=yerror,fmt='bo-', label='therm')
    title = 'centrality='+centrality+'%,  rejection='+rejection.replace('00', '0.0')
    ax.set_title(title)
    ax.legend()
    ax.grid(True)
    #plt.show()        
    plt.savefig(outfile)
    plt.close()
    plt.close('all')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    if len(sys.argv) > 3: configuration = read_config(sys.argv[3])
    else: configuration = read_config()
    datafile, figfile = sys.argv[1:3]

    plot(configuration,datafile,figfile)
