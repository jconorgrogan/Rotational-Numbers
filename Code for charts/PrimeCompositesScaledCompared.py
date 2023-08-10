import numpy as np
import matplotlib.pyplot as plt

def generate_numbers(n, prime=True):
    numbers = []
    candidate = 2 if prime else 4
    while len(numbers) < n:
        if prime:
            is_valid = all(candidate % divisor != 0 for divisor in numbers)
        else:
            is_valid = any(candidate % divisor == 0 for divisor in range(2, candidate))
        if is_valid:
            numbers.append(candidate)
        candidate += 1
    return numbers

def match_composites_to_primes(primes, limit):
    composites = []
    candidate = 4
    prime_index = 0
    while candidate <= limit and prime_index < len(primes):
        is_composite = any(candidate % divisor == 0 for divisor in range(2, candidate))
        if is_composite:
            if len(composites) < prime_index:
                composites.append(candidate)
            else:
                # Stretching: Adding composites to match the current prime index
                while len(composites) < prime_index:
                    composites.append(candidate)
        if candidate >= primes[prime_index]:
            prime_index += 1
        candidate += 1
    return composites

def plot_intersecting_circles(numbers, ax, scaling_factor, node_size=5):
    for idx, number in enumerate(numbers):
        random_offset = np.random.uniform(0, 2 * np.pi)
        angles = np.linspace(0, 2 * np.pi, number, endpoint=False) + random_offset
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
composites_to_plot = match_composites_to_primes(primes_to_plot, 541)

scaling_factor_primes = 1
scaling_factor_composites = 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(100, 50), facecolor='black')
plot_intersecting_circles(primes_to_plot, ax1, scaling_factor_primes, node_size=5)
ax1.set_title("Primes to 100", fontsize=30, color='white')
plot_intersecting_circles(composites_to_plot, ax2, scaling_factor_composites, node_size=5)
ax2.set_title("Matched Composites to 541", fontsize=30, color='white')

plt.savefig('plot_comparison.jpeg', format='jpeg', dpi=500, facecolor='black')
plt.show()
