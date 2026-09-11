import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-6,6,400)
fig,ax=plt.subplots()
for m,label in [(1,r'$y=x$'),(5,r'$y=5x$'),(1/5,r'$y=x/5$')]: 
    ax.plot(x,m*x,label=label)

ax.scatter([0],[0],color=['tab:orange'],zorder=3)
ax.axhline(0,color='black',lw=.7)
ax.axvline(0,color='black',lw=.7)
ax.set(xlim=(-6,6),ylim=(-6,6),xlabel=r'$x$',ylabel=r'$y$')
ax.grid(True,alpha=.3) 
ax.legend()
plt.show()