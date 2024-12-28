import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import random

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()
n = 24 # number of traingles
r = 10 # radius of the outer circle
l = 20 # number of layers
current_r = r

def radius_smaller_circle (r,n):
        theta = 2*np.pi/n # calculate the angle of the first of n points 
        theta1 = 2*2*np.pi/n # calculate the angle of the next point
        x1 = r*np.cos(theta) # x coordinate of first point
        y1 = r*np.sin(theta) # y coordinate of first point
        x2 = r*np.cos(theta1) # x coordinate of second point
        y2 = r*np.sin(theta1) # y coordinate of second point 
        h = np.sqrt(3)*np.sqrt((x2-x1)**2+(y2-y1)**2)/2
        r1 = r - h # calculate the radius of the smaller circle
        return [h,r1]

def draw_triangles_around_circle(r,n):
    for i in range(n):
        theta = i*2*np.pi/n # calculate the angle of the first of n points 
        theta1 = (i+1)*2*np.pi/n # calculate the angle of the next point
        x1 = r*np.cos(theta) # x coordinate of first point
        y1 = r*np.sin(theta) # y coordinate of first point
        x2 = r*np.cos(theta1) # x coordinate of second point
        y2 = r*np.sin(theta1) # y coordinate of second point 
        r1 = radius_smaller_circle (r,n)[1]
        x3 = r1*np.cos((theta+theta1)/2) # x coordinate of the third vertex
        y3 = r1*np.sin((theta+theta1)/2) # y coordinate of the third vertex
        vertices = np.array([[x1, y1], [x2, y2], [x3, y3]]) # all the vertices are grouped
        polygon = Polygon (vertices, facecolor=random_hex_color(), edgecolor='black') # draws the polygon
        axes.add_patch(polygon)

for i in range(l):
     current_r -= radius_smaller_circle(current_r,n)[0]
     draw_triangles_around_circle(current_r,n)
    
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
