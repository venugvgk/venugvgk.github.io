import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

p = 10000
x_min, x_max = -15, 15
y_min, y_max = -15, 15
side = (x_max - x_min) / 3

# Bottom-left corners of the eight cells surrounding the missing center cell.
targets = [
    (x_min + column * side, y_min + row * side)
    for row in range(3)
    for column in range(3)
    if (column, row) != (1, 1)
]

# The next point is always calculated from the previous point.
x, y = random.uniform(x_min, x_max), random.uniform(y_min, y_max)
x_points, y_points = [], []
for iteration in range(p + 20):
    target_x, target_y = random.choice(targets)
    x = target_x + (x - x_min) / 3
    y = target_y + (y - y_min) / 3
    if iteration >= 20:
        x_points.append(x)
        y_points.append(y)

ax.scatter(x_points, y_points, s=0.5, color="blue", marker="s")

# Set the figure area square
ax.set_aspect(1)

# Set axes limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Hide axes labels
ax.set_xticks([])
ax.set_yticks([])

# Remove the border
for spine in ax.spines.values():
    spine.set_visible(False)

plt.show()

