from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division


import numpy as np
import m_tools as MT
import os
# parameters
pm=dict()
""" Standard parameters for ACC-like
    2-layer simulation """
year = 24*60*60*360.

pm['key_name']='exp01'
# grid size parameters
pm['nx']=128#256,                     # grid resolution
pm['ny']=128#256,
pm['L']=6e6#16e6,                     # domain size is L [m]
pm['W']=6e6#16e6,#72e6,
# timestepping parameters
pm['dt']=7200./2.0                   # numerical timestep
pm['twrite']=1000 # interval for cfl and ke writeout (in timesteps)
pm['tmax']=3*year           # total time of integration
pm['tavestart']=1*year       # start time for averaging
pm['taveint']=86400.             # time interval used for summation in longterm average in seconds
#useAB2=False,               # use second order Adams Bashforth timestepping instead of 3rd

# friction parameters
pm['rek']=5.787e-7              # linear drag in lower layer
pm['filterfac']=23.6             # the factor for use in the exponential filter
# constants
#f = None,                   # coriolis parameter (not necessary for two-layer model
                            #  if deformation radius is provided)
pm['g']= 9.81                    # acceleration due to gravity


# diagnostics parameters
pm['diagnostics_list']='all'     # which diagnostics to output
# fft parameters
# removed because fftw is now manditory
#use_fftw = False,               # fftw flag
#teststyle = False,            # use fftw with "estimate" planner to get reproducibility
pm['ntd'] =1 # int(ncors),                       # number of threads to use in fftw computations
#log_level = 1,                 # logger level: from 0 for quiet (no log) to 4 for verbose
#                               #     logger (see  https://docs.python.org/2/library/logging.html)
pm['logfile'] = None                # logfile; None prints to screen


pm['beta']=1.6e-11               # gradient of coriolis parameter
# in Naburos model: delta = 4.4e-18  !linear devrease in beta (1/(s*m*m))

#rek=5.787e-7,               # linear drag in lower layer
pm['rd']=15000.0     # deformation radius
pm['delta']=.25                 # layer thickness ratio (H1/H2)
pm['H1'] = 500                   # depth of layer 1 (H1) in m (?)
pm['U1']=0.2                   # upper layer flow
pm['U2']=0.0                     # lower layer flow

cwd = os.getcwd()
name='SO_standard'
MT.json_save(name, cwd, pm, verbose=True, return_name=False)
