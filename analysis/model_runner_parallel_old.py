import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

import os
import h5py
import sys
import imp

import pyqg
print('use pyqg from: ' + pyqg.__file__)

## read inputs
sys.path.append('/project2/rossby/group07/functions/')
import Saving

if len(sys.argv) <= 1:
    ncors=1
elif sys.argv[1] == '-f':
    ncors=1
else:
    ncors=sys.argv[1]

print('numer of coures ' + str(ncors) )
#base_path='/Projects/2018_Rossbypalooza/'
base_path='/project2/rossby/group07/'
key_name='exmp1'
save_path=base_path+'pyqg_output/'+key_name
plot_path=base_path+'pyqg_output/'+key_name


#import LH95_params

#
# Simulation
#

# the basic parameters
#params = LH95_params.LHTwoLayer()
year = 24*60*60*360.

#m = pyqg.QGModel(beta=1.5e-11, rd=15000.0, delta=0.25, H1=500, U1=0.025, U2=0.0, tmax=3*year)
m = pyqg.QGModel(
        # grid size parameters
        nx=128,#256,                     # grid resolution
        ny=128,#256,
        L=6e6,#16e6,                     # domain size is L [m]
        W=6e6,#16e6,#72e6,
        # timestepping parameters
        dt=7200./2.0,                   # numerical timestep
        twrite=1000, # interval for cfl and ke writeout (in timesteps)
        tmax=3*year,           # total time of integration
        tavestart=1*year,       # start time for averaging
        taveint=86400.,             # time interval used for summation in longterm average in seconds
        #useAB2=False,               # use second order Adams Bashforth timestepping instead of 3rd

        # friction parameters
        rek=5.787e-7,               # linear drag in lower layer
        filterfac=23.6,             # the factor for use in the exponential filter
        # constants
        #f = None,                   # coriolis parameter (not necessary for two-layer model
                                    #  if deformation radius is provided)
        g= 9.81,                    # acceleration due to gravity


        # diagnostics parameters
        diagnostics_list='all',     # which diagnostics to output
        # fft parameters
        # removed because fftw is now manditory
        #use_fftw = False,               # fftw flag
        #teststyle = False,            # use fftw with "estimate" planner to get reproducibility
        ntd = int(ncors),                       # number of threads to use in fftw computations
        #log_level = 1,                 # logger level: from 0 for quiet (no log) to 4 for verbose
        #                               #     logger (see  https://docs.python.org/2/library/logging.html)
        logfile = None,                # logfile; None prints to screen


        beta=1.6e-11,               # gradient of coriolis parameter
        # in Naburos model: delta = 4.4e-18  !linear devrease in beta (1/(s*m*m))

        #rek=5.787e-7,               # linear drag in lower layer
        rd=15000.0,     # deformation radius
        delta=.25,                 # layer thickness ratio (H1/H2)
        H1 = 500,                   # depth of layer 1 (H1) in m (?)
        U1=0.2,                   # upper layer flow
        U2=0.0,                     # lower layer flow
        )


# In[] initializing, does not work jet
# def init_condition(model,sig=1.e-7):
#     """ White noise spectrum with amplitude sig """
#     return sig*np.random.randn(model.nz,model.nx,model.ny)
# def set_q(self,q):
#
#     """ Initialize the potential vorticity.
#
#     Parameters
#     ----------
#     q: an array of floats of dimension (nx,ny):
#             The potential vorticity in physical space.
#     """
#
#     self.q = q
#     self.qh = self.fft(self.q)
#     self._invert()
#     self._calc_rel_vorticity()
#     self.u, self.v = self.ifft(-self.il*self.ph).real, self.ifft(self.ik*self.ph).real
#     self.Ke = self.ke = self._calc_ke_qg()
#
# initial=init_condition(m, sig=1.e-2)
# # q[0]=1e-7*np.random.rand(m.ny,m.nx) + 1e-6*(
# #     np.ones((m.ny,1)) * np.random.rand(1,m.nx) )
# # q[1]=np.zeros_like(m.x)
#
# set_q(m,initial)


#m.set_q1q2(initial[0],initial[1], check=True)
#m.set_q(init_condition(m, sig=1.e-2))
#init_condition(m, sig=1.e-2).shape

# In[]
"""
configure saveing
save_to_disk: bool (optional)
        If True, then save parameters and snapshots to disk.
overwrite: bool (optional)
        If True, then overwrite extant files.
tsave_snapshots: integer (optional)
        Save snapshots every tsave_snapshots time steps.
tdiags: integer (optional)
        Calculate diagnostics every tdiags time steps.
path: string (optional)
        Location for saving output files.
"""
m.save_to_disk=True
m.overwrite = True
m.tsave_snapshots = 10
m.tsnaps=m.tsave_snapshots
m.tdiags = 10
#m.path=base_path+"/outout2"
fields=['t','q']

# just for testing
m.tmax = m.tmax*5.0

ke = []
t = []
k = 1

kmean = 0
Saving.initialize_save_snapshots(m,save_path)

for i in m.run_with_snapshots(tsnapstart=0, tsnapint=10000):

    ke.append(m._calc_ke())
    t.append(m.t)

    if m._calc_cfl()> .3:
        m.dt = m.dt/5.

    Saving.save_snapshots(m, fields=fields)


Saving.save_diagnostics(m)
Saving.save_setup(m)
