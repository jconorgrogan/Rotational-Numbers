import numpy as np
import matplotlib.pyplot as plt

def generate_numbers(n, prime=True):
    numbers = []
    candidate = 2 if prime else 3
    while len(numbers) < n:
        if prime:
            is_valid = all(candidate % divisor != 0 for divisor in numbers)
        else:
            is_valid = any(candidate % divisor == 0 for divisor in range(2, candidate))
            if candidate % 2 == 0: # Exclude even numbers
                is_valid = False
        if is_valid:
            numbers.append(candidate)
        candidate += 1 if prime else 2 # Increment by 2 for non-prime odds to skip even numbers
    return numbers

def plot_intersecting_circles(numbers, ax, scaling_factor, node_size=5):
    for idx, number in enumerate(numbers):
        angles = np.linspace(0, 2 * np.pi, number, endpoint=False)  # Fixed starting point
        radius = (idx + 2) * scaling_factor
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        ax.scatter(x, y, s=node_size, color='white')

    max_radius = (len(numbers) + 1) * scaling_factor
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.axis('off')

primes_to_plot = generate_numbers(100, prime=True)
non_prime_odds_to_plot = generate_numbers(100, prime=False)

scaling_factor_primes = 1
scaling_factor_non_prime_odds = 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(100, 50), facecolor='black')
plot_intersecting_circles(primes_to_plot, ax1, scaling_factor_primes, node_size=5)
ax1.set_title("Primes to 100", fontsize=30, color='white')
plot_intersecting_circles(non_prime_odds_to_plot, ax2, scaling_factor_non_prime_odds, node_size=5)
ax2.set_title("Non-Prime Odds to 100", fontsize=30, color='white')

plt.savefig('plot_comparison.jpeg', format='jpeg', dpi=500, facecolor='black')
plt.show()
