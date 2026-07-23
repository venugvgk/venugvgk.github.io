import random
import matplotlib.pyplot as plt

NUM_TRIALS = 216

# Simulate 216 tosses of two dice and record the sum for each toss.
sums = []
for _ in range(NUM_TRIALS):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sums.append(die1 + die2)

# Count the frequency of each possible sum from 2 to 12.
sum_counts = {total: 0 for total in range(2, 13)}
for total in sums:
    sum_counts[total] += 1

# Prepare data for plotting.
values = list(sum_counts.keys())
frequencies = [sum_counts[total] for total in values]

plt.figure(figsize=(8, 5))
plt.bar(values, frequencies, color="skyblue", edgecolor="black")
plt.title(f"Frequency of Two-Dice Sums over {NUM_TRIALS} Tosses")
plt.xlabel("Sum of two dice")
plt.ylabel("Frequency")
plt.xticks(values)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

# Optionally show the plot and save it.
plt.show()
