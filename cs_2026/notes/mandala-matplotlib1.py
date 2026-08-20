import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

figure, axes = plt.subplots()
sides = 5
radius = 10
theta = 2 * np.pi/sides
r = radius

for r in range(radius):
    vertices = []
    for i in range(sides):
        angle = i * theta
        vertices.append((r * np.cos(angle), r * np.sin(angle)))

    polygon = Polygon(vertices, facecolor='none', edgecolor='black')
    axes.add_patch(polygon)
   
# Set the figure area square
axes.set_aspect(1)

# Set axes limits
axes.set_xlim(-2*radius, 2*radius)
axes.set_ylim(-2*radius, 2*radius)

# Hide axes labels
axes.set_xticks([])
axes.set_yticks([])

# Remove the border
for spine in axes.spines.values():
    spine.set_visible(False)

plt.show()

