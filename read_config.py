#!/usr/bin/env python
import os
import sys

def read_config(cfile='config'):
    params = ['fit_input_dir', 'fit_output_dir_core', 'atlas_data_dir', 'centrality', 'rejection']
    params_with_slash = ['fit_input_dir', 'atlas_data_dir']
    configuration = dict( zip(params, ['']*len(params)) )
    if os.path.exists(cfile):
        with open(cfile) as file:
            for line in file:
                if line.startswith('#'): continue
                if '=' not in line: continue
                for param in configuration.keys():
                    if line.startswith(param):
                        value = line.split('=')[1].strip()
                        if param in params_with_slash and not value.endswith('/'): 
                            print 'read_config: adding slash \"/\" to parameter: \"{}\"'.format(param)
                            value = value+'/'
                        configuration[param] = value
                        break
                new_param_name, value = line.split('=')
                new_param_name, value = new_param_name.strip(), value.strip()
                if new_param_name in configuration.keys(): continue
                if 'dir' in param and not value.endswith('/'): 
                    print 'WARNING:'+sys.argv[0]+': unknown parameter with \'dir\' in its name: \"{}\" \t NOT ending with slash'.format(param)
                print 'new param: \"{}\"   with value: {}'.format(new_param_name, value)
                configuration[new_param_name] = value
    else:
         print 'ERROR: no config file'
         sys.exit()

    configuration['fit_output_dir'] = ( 'cent'+configuration['centrality']+'/'+
                                        configuration['fit_output_dir_core']+
                                        '_reject'+configuration['rejection']+'/' )

    print 'loaded configuration:\n',configuration
    return configuration
