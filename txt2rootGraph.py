import numpy as np
import ROOT
import sys
from read_config import read_config

fig_lst = ['23a', '23b', '24a', '24b', '25a', '25b', '29a', '29b', '34a']
var_lst = ['rout_m1zero', 'rout_1a', 'rside_m1zero', 'rside_1a', 'rlong_m1zero', 'rlong_1a', 'lambda_m1zero', 'lambda_1a', 'routlong_1a']

fig_var_dict = dict(zip(fig_lst,var_lst))
var_fig_dict = dict(zip(var_lst,fig_lst))


if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
else: configuration = read_config()
atlas_dir = configuration['atlas_data_dir']
therm_dir = configuration['fit_output_dir'] 
centrality = configuration['centrality']
rejection = configuration['rejection']

therm_dir_low  = therm_dir.replace('reject'+rejection, 'reject002')
therm_dir_med  = therm_dir.replace('reject'+rejection, 'reject0025')
therm_dir_high = therm_dir.replace('reject'+rejection, 'reject003')



for var,fig in zip(var_lst,fig_lst):
    print fig, var

    # # #
    # therminator2 graph
    # # #
    f2  = open(therm_dir_low  +var+'.dat')
    f25 = open(therm_dir_med  +var+'.dat')
    f3  = open(therm_dir_high +var+'.dat')
    
    val2, val25, val3 = [],[],[]
    rapid = [-2,-1,0,1,2]
    kt = [0.25, 0.35, 0.45, 0.55, 0.65, 0.75]
    
    for file,vals in zip([f2,f25,f3], [val2,val25,val3]):
        for line in file:
            if 'zero' in line: continue
            v = float(line.split()[1].strip())
            vals.append(v)
        file.close()

    assert len(val2) == len(val25)
    assert len(val2) == len(val3)
    
    therm_graph = ROOT.TGraphAsymmErrors(len(val25))
    
    if '1a' in var: 
        xaxis = rapid
        xerr = 0.5 
    else: 
        xaxis = kt
        xerr = 0.05

    for i,point in enumerate(zip(xaxis,val2,val25,val3)):
        xax,v2,v25,v3 = point
        therm_graph.SetPoint(i,xax, v25)
        therm_graph.SetPointError(i, xerr,xerr, v25-min(v2,v3), max(v2,v3)-v25 )


    # # #
    # ATLAS graph
    # # #
    x_lst,y_lst = [],[]
    file = open(atlas_dir+'fig_'+fig+'_cent'+centrality+'.dat')
    for line in file:
        if line.startswith('#'): continue
        if len(line.split()) < 2: continue
        x,y = line.split()
        x,y = float(x.strip()), float(y.strip())
        x_lst.append(x)
        y_lst.append(y)

    file.close()
    x_lst = np.array(x_lst)
    y_lst = np.array(y_lst)

    # order in file: points, upper left, lower right
    n_points = len(x_lst)/3
    x_points = x_lst[:n_points]
    x_low_err = x_points - x_lst[n_points:2*n_points]
    x_high_err = x_lst[2*n_points:] - x_points

    y_points = y_lst[:n_points]
    y_high_err = y_lst[n_points:2*n_points] - y_points
    y_low_err = y_points - y_lst[2*n_points:]

    atlas_graph = ROOT.TGraphAsymmErrors(n_points)
    
    for i,point in enumerate(zip(x_points,y_points, x_low_err,x_high_err, y_low_err, y_high_err )):
        atlas_graph.SetPoint(i,point[0], point[1])
        atlas_graph.SetPointError(i, point[2], point[3], point[4], point[5])

    # # #
    # save to file
    # # #
    rootfile = ROOT.TFile('therm_atlas_comparision/fig_'+fig+'.root', 'UPDATE')

    therm_graph.SetName('therm2'+centrality)
    therm_graph.Write() 
    atlas_graph.SetName('atlas'+centrality)
    atlas_graph.Write()

    del(therm_graph)
    del(atlas_graph)
    rootfile.Close()
