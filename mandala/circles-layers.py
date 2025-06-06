#| label: circles
import numpy as np
import matplotlib.pyplot as plt
import random
import math

def random_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

figure, axes = plt.subplots()

r = 20 #radius of center circle
n = 24 # number of circles around 
num_layers = 15  # Number of layers of circles to draw
current_r = r

#calculate the radius of the smaller circles

def calc_r_small(r,n):
    theta1 = (2*np.pi)/n
    x2 = r*np.cos(theta1)
    y2 = r*np.sin(theta1)
    r_small = math.sqrt((x2-r)**2+(y2)**2)/2
    return(r_small)

# Draw n circles with random colors and add to the plot - shift_theta shifts starting angle by .5 times theta for odd layers
def draw_n_circles(r, n, shift_theta=False):
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    if shift_theta:
        theta += (np.pi / n)  # Shift by 0.5 theta
    for t in theta:
        x = r * np.cos(t)
        y = r * np.sin(t)
        color = random_hex_color()
        r_small = calc_r_small(r,n)
        draw_circle = plt.Circle((x, y), r_small, fill=True, edgecolor='black',facecolor=color,alpha=0.2)
        axes.add_artist(draw_circle)
    
# calculate subsequent radii and draw for the number of layers

for i in range(num_layers):
    shift_theta = (i % 2 == 1)  # Shift theta for odd layers
    current_r -= 1.6 * calc_r_small(current_r, n)
    draw_n_circles(current_r, n, shift_theta)


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