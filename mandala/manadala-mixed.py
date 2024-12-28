import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random
import math

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
figure, axes = plt.subplots()

r = 10 #radius of outer circle
flower_size = 0.3
num_petals = 12
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
        vertices = [(x1,y1),(x2,y2),(0,0),(x3,y3)]
        polygon = Polygon (vertices,facecolor=random_hex_color(),edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)

central_flower(flower_size,num_petals)

def draw_triangles(r1,r2,num_triangle,num_layers): #draws triangles in circles in given layers between r1 and r2
    h = (r2-r1)/num_layers
    for i in range(num_layers-1):
        r_first = r1 + i*h
        r_next = r1 + (i+1)*h
        








        
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