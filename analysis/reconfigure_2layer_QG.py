
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')

import imp
import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
#sys.path.append('/project2/rossby/group07/')
#pyqg=imp.load_source('__init__.py', '/project2/rossby/group07/pyqg_pip/')
#pyqg.QGModel=imp.load_source('QGModel.py', '/project2/rossby/group07/pyqg_pip/')
#pyqg=imp.find_module('__init__.py', '/project2/rossby/group07/pyqg_pip/')
#pyqg=imp.find_module('s', '/project2/rossby/group07/pyqg_pip/')


# In[2]:


sys.path


# In[3]:


#!export PYTHONPATH=/project2/rossby/group07
import pyqg_pip as pyqg
pyqg.__file__


# In[4]:


year = 24*60*60*360.
m = pyqg.QGModel(beta=1.5e-11, rd=15000.0, delta=0.25, H1=500, U1=0.025, U2=0.0)
#m.run()


# In[5]:


# q_upper = m.q[0] + m.Qy[0]*m.y
# plt.contourf(m.x, m.y, q_upper, 12, cmap='RdBu_r')
# plt.xlabel('x'); plt.ylabel('y'); plt.title('Upper Layer PV')
# plt.colorbar();


# In[35]:


imp.reload(pyqg)
year = 24*60*60*360.
m = pyqg.QGModel(    
        # grid size parameters
        nx=128#256,                     # grid resolution
        ny=128#256,
        L=16e6,                     # domain size is L [m]
        W=16e6#72e6,
        # timestepping parameters
        dt=7200.,                   # numerical timestep
        twrite=10000, # interval for cfl and ke writeout (in timesteps)
        tmax=1*year,           # total time of integration
        tavestart=5*year,       # start time for averaging
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
        ntd = 1,                       # number of threads to use in fftw computations
        #log_level = 1,                 # logger level: from 0 for quiet (no log) to 4 for verbose
        #                               #     logger (see  https://docs.python.org/2/library/logging.html)
        logfile = None,                # logfile; None prints to screen
        
        
        beta=1.6e-11,               # gradient of coriolis parameter
        # in Naburos model: delta = 4.4e-18  !linear devrease in beta (1/(s*m*m))
    
        #rek=5.787e-7,               # linear drag in lower layer
        rd=800000.0,                 # deformation radius
        delta=1,                 # layer thickness ratio (H1/H2)
        H1 = 500,                   # depth of layer 1 (H1) in m (?)
        #U1=0.025,                   # upper layer flow
        U2=0.0,                     # lower layer flow
        )


# In[37]:


xx, yy= np.meshgrid(np.arange(m.nx),np.arange(m.ny))


# In[38]:


sigma=.2
mu=0
bins=(yy-round(m.ny/2))/m.ny
yy_new=1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2))


# In[39]:


plt.contourf(yy_new)
plt.colorbar()


# In[40]:


m.set_q1q2(yy_new, yy_new*0)


# In[41]:


m.run()


# In[42]:


q_upper = m.q[0] + m.Qy[0]*m.y
plt.contourf(m.x, m.y, q_upper, 12, cmap='RdBu_r')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Upper Layer PV')
plt.colorbar();


# In[12]:


kespec_u = m.get_diagnostic('KEspec')[0].sum(axis=0)
kespec_l = m.get_diagnostic('KEspec')[1].sum(axis=0)
plt.loglog( m.kk, kespec_u, '.-' )
plt.loglog( m.kk, kespec_l, '.-' )
plt.legend(['upper layer','lower layer'], loc='lower left')
plt.ylim([1e-9,1e-3]); plt.xlim([m.kk.min(), m.kk.max()])
plt.xlabel(r'k (m$^{-1}$)'); plt.grid()
plt.title('Kinetic Energy Spectrum');

