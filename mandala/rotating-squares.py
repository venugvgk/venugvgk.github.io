import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import random

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()

s = 10  # side length of the initial square
rot = 15 # set to 2, to rotate 90 degrees. larger values rotate by smaller degrees
# the side of each square is divided into rot:1 ratio 
num_layers = 5*rot  # Number of layers of squares to draw

# Initial coordinates of the square
x1, y1 = s, s
x2, y2 = -s, s
x3, y3 = -s, -s
x4, y4 = s, -s

for i in range(num_layers):
    # Draw the square
    vertices = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    p = Polygon(vertices, facecolor=random_hex_color(), edgecolor='black')
    axes.add_patch(p)
    
    # Calculate the midpoints for the next square
    new_x1, new_y1 = (x1*(rot-1) + x2) / rot, (y1*(rot-1) + y2) / rot
    new_x2, new_y2 = (x2*(rot-1) + x3) / rot, (y2*(rot-1) + y3) / rot
    new_x3, new_y3 = (x3*(rot-1) + x4) / rot, (y3*(rot-1) + y4) / rot
    new_x4, new_y4 = (x4*(rot-1) + x1) / rot, (y4*(rot-1) + y1) / rot
    
    # Update the coordinates for the next iteration
    x1, y1 = new_x1, new_y1
    x2, y2 = new_x2, new_y2
    x3, y3 = new_x3, new_y3
    x4, y4 = new_x4, new_y4

# Set the figure area square
axes.set_aspect(1)

# Set axes limits
axes.set_xlim(-s, s)
axes.set_ylim(-s, s)

# Hide axes labels
axes.set_xticks([])
axes.set_yticks([])

plt.show()