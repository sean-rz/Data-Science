import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

x = np.arange(0,100)
y = x * 2
z = x ** 2


fig = plt.figure()   # figure object

ax1 = fig.add_axes([0, 0, 1, 1])
# ax1 = fig.add_subplot(111)
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])

ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.tick_params(direction='in') # or out 

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)


# Subplots

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))
axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='-')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')

fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

plt.show()