import numpy as np
import matplotlib.pyplot as plt
import random

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()
r = 10
draw_center_circle=plt.Circle((0,0),10, fill=False, edgecolor='white')

# Draw 24 circles with random colors
for i in range(6):
    theta = i * (2 * np.pi / 6)
    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta)
    color = random_hex_color()
    print (color)
    draw_circle = plt.Circle((x1, y1), r, fill=True, edgecolor='black',facecolor=color,alpha=0.2)
    axes.add_artist(draw_circle)


axes.add_artist(draw_center_circle)

axes.set_aspect(1)
axes.set_xlim(-2*r, 2*r)
axes.set_ylim(-2*r, 2*r)

# Hide axes labels
axes.set_xticks([])
axes.set_yticks([])

# Remove the border
for spine in axes.spines.values():
    spine.set_visible(False)

plt.show()