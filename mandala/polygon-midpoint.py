import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()
r = 10  # radius of the circumcircle of the polygon
n = 8  # number of sides of the polygon
num_layers = 7*n # number of layers of polygons to draw

# Function to calculate midpoints of a polygon
def calculate_midpoints(vertices):
    midpoints = []
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        midpoints.append([mid_x, mid_y])
    return np.array(midpoints)

# Generate initial polygon vertices
theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
vertices = np.array([[r * np.cos(t), r * np.sin(t)] for t in theta])

# Draw polygons
for _ in range(num_layers):
    polygon = Polygon(vertices, closed=True, facecolor=random_hex_color(), edgecolor='black')
    axes.add_patch(polygon)
    vertices = calculate_midpoints(vertices)

# Set the figure area square
axes.set_aspect(1)

# Set axes limits
axes.set_xlim(-r, r)
axes.set_ylim(-r, r)

# Hide axes labels
axes.set_xticks([])
axes.set_yticks([])

# Remove the border
for spine in axes.spines.values():
    spine.set_visible(False)

plt.show()