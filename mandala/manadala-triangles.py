import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random
 

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()
r = 15
r1 = 5 #radius of the central flower
r_petal = 0.3*r1 # length of the petal lower edge
r2 = r1 + 2 # radius of the first layer of figures
r3 = r1 + 4 # radius of the second layer of figures 
r4 = r1 + 6 # radius of the third layer of figures
r5 = r1 + 8 # radius of the fourth layer of figures
r6 = r1 + 10 # radius of the fifth layer of figures
num_petals = 10 # number of petals in the central flower 
theta = np.linspace(0,2*np.pi,num_petals,endpoint=False) # divides the circle into equal angles for the petals
delta = np.pi/num_petals # half of the angle between each petal


def central_flower(): 
    
    for t in theta:
        x1 = r1*np.cos(t)
        y1 = r1*np.sin(t)
        x2 = r_petal*np.cos(t+2*delta)
        y2 = r_petal*np.sin(t+2*delta)
        x3 = r_petal*np.cos(t-2*delta)
        y3 = r_petal*np.sin(t-2*delta)
        petal_vertices = [(x1,y1),(x2,y2),(0,0),(x3,y3)]
        polygon = Polygon (petal_vertices,facecolor=random_hex_color(),edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)

def first_layer_of_figures():
    for t in theta:
        x1 = r1*np.cos(t)
        y1 = r1*np.sin(t)
        x2 = r1*np.cos(t+2*delta)
        y2 = r1*np.sin(t+2*delta)
        x3 = r2*np.cos(t+delta)
        y3 = r2*np.sin(t+delta) 
        polygon_vertices = [(x1,y1),(x2,y2),(x3,y3)]
        polygon = Polygon(polygon_vertices, facecolor=random_hex_color(), edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)


def second_layer_of_figures():
    for t in theta:
        x1 = r2*np.cos(t+delta)
        y1 = r2*np.sin(t+delta)
        x2 = r2*np.cos(t+3*delta)
        y2 = r2*np.sin(t+3*delta)
        x3 = r3*np.cos(t+2*delta)
        y3 = r3*np.sin(t+2*delta) 
        polygon_vertices = [(x1,y1),(x2,y2),(x3,y3)]
        polygon = Polygon(polygon_vertices, facecolor=random_hex_color(), edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)


def third_layer_of_figures():
    for t in theta:
        x1 = r3*np.cos(t+2*delta)
        y1 = r3*np.sin(t+2*delta)
        x2 = r3*np.cos(t+4*delta)
        y2 = r3*np.sin(t+4*delta)
        x3 = r4*np.cos(t+3*delta)
        y3 = r4*np.sin(t+3*delta) 
        polygon_vertices = [(x1,y1),(x2,y2),(x3,y3)]
        polygon = Polygon(polygon_vertices, facecolor=random_hex_color(), edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)


def fourth_layer_of_figures():
    for t in theta:
        x1 = r4*np.cos(t+3*delta)
        y1 = r4*np.sin(t+3*delta)
        x2 = r4*np.cos(t+5*delta)
        y2 = r4*np.sin(t+5*delta)
        x3 = r5*np.cos(t+4*delta)
        y3 = r5*np.sin(t+4*delta) 
        polygon_vertices = [(x1,y1),(x2,y2),(x3,y3)]
        polygon = Polygon(polygon_vertices, facecolor=random_hex_color(), edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)

def fifth_layer_of_figures():
    for t in theta:
        x1 = r5*np.cos(t+4*delta)
        y1 = r5*np.sin(t+4*delta)
        x2 = r5*np.cos(t+6*delta)
        y2 = r5*np.sin(t+6*delta)
        x3 = r6*np.cos(t+5*delta)
        y3 = r6*np.sin(t+5*delta) 
        polygon_vertices = [(x1,y1),(x2,y2),(x3,y3)]
        polygon = Polygon(polygon_vertices, facecolor=random_hex_color(), edgecolor='black', alpha=0.2)
        axes.add_artist(polygon)

central_flower()
first_layer_of_figures()
second_layer_of_figures()
third_layer_of_figures()
fourth_layer_of_figures()
fifth_layer_of_figures()








        
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