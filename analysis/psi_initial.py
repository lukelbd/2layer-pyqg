import numpy as np

def psi_initial(nx,ny,dx,dy,umax,k):
    ymax = ny*dy
    xmax = nx*dx
    x = np.linspace(0,xmax,nx)
    y = np.linspace(0,ymax,ny)
    xx, yy = np.meshgrid(x,y)
    psi = 4*(umax*ymax/k)/(1 + np.exp(-k*((yy/ymax)-0.5)))
    return psi

# Use the bottom version if you've already constructed yy
# in the set up script
def psi_init(yy,umax,k):
    ymax = np.max(yy)
    psi = 4*(umax*ymax/k)/(1 + np.exp(-k*((yy/ymax)-0.5)))
    return psi
