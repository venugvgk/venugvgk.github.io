import random
import matplotlib.pyplot as plt

TRIAL_SIZES = [36, 216, 1296, 7776]


def simulate_dice_sums(num_trials):
    """Simulate num_trials throws of two dice and return a list of sums."""
    sums = []
    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)
    return sums


def count_sum_frequencies(sums):
    """Count how often each sum from 2 to 12 appears."""
    sum_counts = {total: 0 for total in range(2, 13)}
    for total in sums:
        sum_counts[total] += 1
    return sum_counts


def theoretical_distribution():
    """Return the theoretical probability distribution for the sum of two dice."""
    counts = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    total = sum(counts)
    return {value: count / total for value, count in zip(range(2, 13), counts)}


def normalize_counts(sum_counts):
    """Convert raw frequencies into probabilities."""
    total = sum(sum_counts.values())
    return {k: v / total for k, v in sum_counts.items()}


def plot_distributions(trial_sizes):
    """Simulate and plot distributions for several trial sizes."""
    values = list(range(2, 13))
    plt.figure(figsize=(10, 6))

    for num_trials in trial_sizes:
        sums = simulate_dice_sums(num_trials)
        sum_counts = count_sum_frequencies(sums)
        probabilities = [normalize_counts(sum_counts)[value] for value in values]
        plt.plot(values, probabilities, marker="o", label=f"{num_trials} tosses")

    theoretical = theoretical_distribution()
    theoretical_probs = [theoretical[value] for value in values]
    plt.plot(values, theoretical_probs, linestyle="--", color="black", label="Theoretical")

    plt.title("Two-Dice Sum Distribution for Different Numbers of Tosses")
    plt.xlabel("Sum of two dice")
    plt.ylabel("Relative frequency")
    plt.xticks(values)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_distributions(TRIAL_SIZES)
