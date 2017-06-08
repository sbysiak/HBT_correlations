#!/usr/bin/env python
import os
import sys

def read_config(cfile='config'):
    params = ['fit_input_dir', 'fit_output_dir']
    configuration = dict( zip(params, ['']*len(params)) )
    if os.path.exists(cfile):
        with open(cfile) as file:
            for line in file:
                if line.startswith('#'): continue
                if '=' not in line: continue
                for param in configuration.keys():
                    if line.startswith(param):
                        value = line.split('=')[1].strip()
                        if not value.endswith('/'): value = value+'/'
                        configuration[param] = value
                        break
                new_param_name, value = line.split('=')
                new_param_name, value = new_param_name.strip(), value.strip()
                if new_param_name in configuration.keys(): continue
                if not value.endswith('/'): value = value+'/'
                print 'new param: {} with value: {}'.format(new_param_name, value)
                configuration[new_param_name] = value
    else:
         print 'WARNING: no config file'
         sys.exit()


    print configuration
    return configuration
