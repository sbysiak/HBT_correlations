#!/usr/bin/env python
import sys
from read_config import read_config
from run_fits import run_fits
from collect_data import collect_data
from plotEmAll import plotEmAll
from txt2rootGraph import txt2rootGraph



if len(sys.argv) > 1: configuration = read_config(sys.argv[1])
else: configuration = read_config()

rejection_lst = ('002', '0025', '003')

for rejection in rejection_lst:
    configuration['rejection'] = rejection
    configuration['fit_output_dir'] = ( 'cent'+configuration['centrality']+'/'+
                                        configuration['fit_output_dir_core']+
                                        '_reject'+configuration['rejection']+'/' )
    run_fits(configuration)
    collect_data(configuration)
    #plotEmAll(configuration)  # optional, if uncommented - comment txt2rootGraph(..) below

txt2rootGraph(configuration, rejection_lst)


