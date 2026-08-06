
"""Example: create a simple dictionary and plot a line graph using matplotlib.

To run: python simple-plots.py
"""
import matplotlib.pyplot as plt

def main():
	# Simple dictionary mapping x -> y
	data = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

	# If keys are not in order, sort them for plotting
	x = sorted(data.keys())
	y = [data[k] for k in x]

	plt.figure(figsize=(6, 4))
	plt.plot(x, y, marker='o', linestyle='-', color='tab:blue')
	plt.title('Line plot from a simple dictionary')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True)
	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	main()
