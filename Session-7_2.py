import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2* np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

mat = plt.subplots(nrows = 2,ncols = 2)
"""
axes[0,0].plot(x,y1)

axes[0,0].set(title = 'avali')
axes[0,1].plot(x,x)
axes[0,1].set(xlim = [0,10])
axes[1,1].plot(x,y2)
"""




"""
fig1 = plt.figure(facecolor = (1,0,0,0.5),figsize = (5,7))
ax1 = fig1.add_subplot(111)
ax1.set(xlabel = 'mehvar x',ylabel = 'mehvare y',title = 'utech',xlim = [0,2],ylim = [-2,8])
ax1.set_xlabel('label jadid')
"""

"""
plt.plot(x,y1,label = 'sin')


plt.plot(x,y2,label = 'cos')
plt.title('class python utech')
plt.xlabel('mehvar x ha')
plt.ylabel('mehvar y ha')
plt.grid()
plt.legend()
"""


