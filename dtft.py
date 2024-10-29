import numpy as np
from matplotlib import pyplot as plt
N=1000
n=np.arange(N)
x=np.sin(2*np.pi*0.1*n)
o=np.linspace(-np.pi,np.pi,0.0001*np.pi)
y=np.array([np.sum(x*np.exp(-1j*w*n)) for w in o])
#magnitude
plt.subplot(2,1,1)
plt.plot(o,np.abs(y))
plt.title('magnitude spectrum')
plt.ylabel('magnitude')
#phase
plt.subplot(2,1,2)
plt.plot(o,np.angle(y))
plt.title('phase spectrum')
plt.xlabel('frequency (rad/sample)')
plt.ylabel('phase (radians)')
