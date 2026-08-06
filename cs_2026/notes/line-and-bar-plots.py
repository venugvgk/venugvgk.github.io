import matplotlib.pyplot as plt

# Create a simple dictionary with categories and values
data = {
    "Apples": 10,
    "Bananas": 15,
    "Cherries": 7,
    "Dates": 12,
    "Elderberries": 5,
}

# Extract keys and values for plotting
categories = list(data.keys())
values = list(data.values())

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue', label='Value (bar)')

# Add a line plot for the same data
plt.plot(categories, values, color='darkorange', marker='o', linestyle='-', label='Value (line)')

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Dictionary Values: Bar and Line Plot')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()