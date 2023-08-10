import numpy as np
import matplotlib.pyplot as plt

def generate_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = all(candidate % prime != 0 for prime in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

def plot_intersecting_circles_simplified(primes, ax):
    max_prime = max(primes)
    node_size = 1

    for idx, prime in enumerate(primes):
        angles = np.linspace(0, 2 * np.pi, prime, endpoint=False)
        radius = np.log(idx + 2)  # Logarithmic scaling for radii
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        circle = plt.Circle((0, 0), radius, color='lightgray', fill=False)
        ax.add_artist(circle)
        ax.scatter(x, y, s=node_size, color='black')

    max_radius = np.log(len(primes) + 1)
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_aspect('equal')
    ax.axis('off')

primes_to_plot_extended = generate_primes(500)
fig, ax = plt.subplots(figsize=(40, 40))
plot_intersecting_circles_simplified(primes_to_plot_extended, ax)
plt.title("Intersecting Circles for First 500 Primes", fontsize=30)
plt.savefig("primes.jpg", dpi=300)
plt.show()
