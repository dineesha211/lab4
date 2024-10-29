import numpy as np
from matplotlib import pyplot as plt
N=6
n=np.arange(N)
x=[1,2,3,4,5,6]
l=len(x)
o=np.linspace(-np.pi,np.pi,100)
for i in range(0,l-1):
  y=np.array([np.sum(x[i]*np.exp(-1j*w*n)) for w in o])
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
plt.show()
