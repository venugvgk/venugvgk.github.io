import numpy as np
import random 
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

p = 30000

vertices = [(-15,-15),(15,-15),(0,15*(np.sqrt(3)-1))]

for x,y in vertices:
    plt.plot(x, y, marker="o", color="red", markersize=1)

x2 = random.uniform(-15.0,15.0)

if x2>=0:
    ymax = int(-15+(15-x2)*np.sqrt(3))
else:
    ymax = int(-15+(15+x2)*np.sqrt(3))

y2 = random.uniform(-15,ymax)

while p > 0:
    i = random.randint(0,2)
    x1,y1 = vertices[i]

    x3 = (x1+x2)/2
    y3 = (y1+y2)/2
    
    plt.plot(x3, y3, marker="o", color="blue", markersize=1)
    x2 = x3
    y2 = y3
    p = p-1

# Set the figure area square
ax.set_aspect(1)

# Set axes limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Hide axes labels
ax.set_xticks([])
ax.set_yticks([])

# Remove the border
for spine in ax.spines.values():
    spine.set_visible(False)

plt.show()

