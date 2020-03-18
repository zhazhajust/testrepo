import numpy as np
import matplotlib.pyplot as plt
import sdf
plt.switch_backend('agg')
freqs=np.loadtxt('freqs.txt')
xf=np.loadtxt('xf.txt')
c       =  3e8
micron  =  1e-6
gridnumber = 1200
stop    =  100
dt_snapshot= 1e-15
x_end   =  60 * micron
x_max   =  60 * micron
x_min   =  0 * micron
window_start_time =  (x_max - x_min) / c
delta_x =  x_end/gridnumber
t_end   =  stop * dt_snapshot
if t_end-window_start_time<0:
      xgrid   =  int(gridnumber)
else:
      xgrid   =  int(gridnumber + c*(t_end-window_start_time)/delta_x)
x=np.arange(xgrid+1)
X,Freqs=np.meshgrid(x,freqs)
Xf=xf.T
fig,ax=plt.subplots()
im=ax.pcolormesh(X,Freqs,Xf,cmap=plt.get_cmap('rainbow'))
fig.colorbar(im,ax=ax)
fig.savefig('Xf.png',dpi=200)
