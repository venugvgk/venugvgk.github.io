from turtle import circle

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import random
import math

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
figure, axes = plt.subplots()

r = 10 #radius of outer circle
flower_size = 0.3
num_petals = 16
outer_polygon_vertices = []
outer_polygon2_vertices = []

def central_flower(size,petals): 
    #size is the size of the flower as a portion of the total picture
    # petals is number of petals                           
    r_flower = r*size
    theta = np.linspace(0,2*np.pi,petals,endpoint=False)

    for t in theta:
        x1 = r_flower*np.cos(t)
        y1 = r_flower*np.sin(t)
        r_petal = r*size*0.3
        x2 = r_petal*np.cos(t+2*np.pi/petals)
        y2 = r_petal*np.sin(t+2*np.pi/petals)
        x3 = r_petal*np.cos(t-2*np.pi/petals)
        y3 = r_petal*np.sin(t-2*np.pi/petals)
        petal_vertices = [(x1,y1),(x2,y2),(0,0),(x3,y3)]
        polygon = Polygon (petal_vertices,facecolor=random_hex_color(),edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)
        outer_polygon_vertices.append((x1,y1))
        
        x4 = (r_flower+1)*np.cos(t+np.pi/petals)
        y4 = (r_flower+1)*np.sin(t+np.pi/petals)
        x5 = r_flower*np.cos(t+2*np.pi/petals)
        y5 = r_flower*np.sin(t+2*np.pi/petals)  
        triangle_vertices = [(x1,y1),(x4,y4),(x5,y5)]
        triangle = Polygon (triangle_vertices,facecolor=random_hex_color(),edgecolor='black', alpha=0.2)
        axes.add_artist(triangle)   
        outer_polygon2_vertices.append((x4,y4))
                
        
central_flower(flower_size,num_petals)

outer_polygon = Polygon (outer_polygon_vertices,edgecolor='black', fill=False,alpha=0.2)
axes.add_artist(outer_polygon)

outer_polygon2 = Polygon (outer_polygon2_vertices,edgecolor='black', fill=False,alpha=0.2)
axes.add_artist(outer_polygon2)



        








        
#set the figure area square
axes.set_aspect(1)

#set axes limits 
axes.set_xlim(-r, r)
axes.set_ylim(-r, r)

# Hide axes labels
axes.set_xticks([])
axes.set_yticks([])

# Remove the border
for spine in axes.spines.values():
    spine.set_visible(False)

plt.show()