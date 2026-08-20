import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

figure, axes = plt.subplots()
sides = 5
radius = 10
theta = 2 * np.pi/sides
r = radius

while r > 0:
    vertices = []
    for i in range(sides+1):
        angle = i * theta
        vertices.append((r * np.cos(angle), r * np.sin(angle)))

    polygon = Polygon(vertices, edgecolor='black')
    axes.add_patch(polygon)

    r = r-2
   
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

figure.savefig('mandala.png', dpi=300, bbox_inches='tight')
plt.show()

