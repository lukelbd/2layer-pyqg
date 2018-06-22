from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import sys
sys.path.append('/project2/rossby/group07/functions/')
import numpy as np
import m_tools as MT
import os

import xarray as xr

key_name='exmp1'
base='/project2/rossby/group07/'
#base='/Projects/mount/'
load_path=base+'pyqg_output/'+key_name+'/'

import os
cwd = os.getcwd()


class experiment(object):

        def __init__(self, path):
            """
            load experiment diagnostiscs
            reutrns:

            self.path
            self.diagnostics
            self.setup
            self.snapshots
            """
            self.path = load_path

            self.diagnostics=xr.open_dataset(load_path+'diagnostics.h5')
            self.setup=xr.open_dataset(load_path+'setup.h5')


        def load_snapshots(self):
            self.snapshots=xr.open_mfdataset(load_path+'snapshots/*.h5')

#snapshots=xr.open_mfdataset(load_path+'snapshots/*.h5')
exp=experiment(load_path)

exp.diagnostics


# In[12]:
m.diagnostics.keys()
kespec_u = exp.diagnostics['KEspec')[0].sum(axis=0)
kespec_l = m.get_diagnostic('KEspec')[1].sum(axis=0)
plt.loglog( m.kk, kespec_u, '.-' )
plt.loglog( m.kk, kespec_l, '.-' )
plt.legend(['upper layer','lower layer'], loc='lower left')
plt.ylim([1e-9,1e-3]); plt.xlim([m.kk.min(), m.kk.max()])
plt.xlabel(r'k (m$^{-1}$)'); plt.grid()
plt.title('Kinetic Energy Spectrum');


# In[]
plt.figure()
plt.plot(t, ke)
plt.xlabel('time'); plt.ylabel('KE'); plt.title('KE')
plt.savefig(plot_path+key_name+'_KE'+'.png', bbox_inches='tight')
# In[]


plt.figure()
q_upper = m.q[0] + m.Qy[0]*m.y
plt.contourf(m.x, m.y, q_upper, 12, cmap='RdBu_r')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Upper Layer PV')
plt.colorbar();
plt.savefig(plot_path+key_name+'_UpperPV'+'.png', bbox_inches='tight')

plt.figure()
q_lower = m.q[1] + m.Qy[1]*m.y
plt.contourf(m.x, m.y, q_upper, 12, cmap='RdBu_r')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Lower Layer PV')
plt.colorbar();
plt.savefig(plot_path+key_name+'_LowerPV'+'.png', bbox_inches='tight')

plt.figure()
speed_upper = np.sqrt(m.u[0]**2, m.v[0]**2)
plt.contourf(m.x, m.y, speed_upper, 12, cmap='RdBu_r')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Upper Layer Speed')
plt.colorbar();
plt.savefig(plot_path+key_name+'_UpperSpeed'+'.png', bbox_inches='tight')
