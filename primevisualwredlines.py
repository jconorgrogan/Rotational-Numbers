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

def plot_intersecting_circles_linear(primes, ax):
    node_size = 10

    # Draw lines radiating from the origin at multiples of pi/4
    for i in range(8):
        angle = i * np.pi / 4
        x_line = np.cos(angle)
        y_line = np.sin(angle)
        ax.plot([0, x_line * len(primes)], [0, y_line * len(primes)], color='red', linestyle='--')

    for idx, prime in enumerate(primes):
        angles = np.linspace(0, 2 * np.pi, prime, endpoint=False)
        radius = idx + 2  # Linear scaling for radii
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        circle = plt.Circle((0, 0), radius, color='lightgray', fill=False)
        ax.add_artist(circle)
        ax.scatter(x, y, s=node_size, color='black')

    max_radius = len(primes) + 1
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_aspect('equal')
    ax.axis('off')

primes_to_plot_extended = generate_primes(50)
fig, ax = plt.subplots(figsize=(40, 40))
plot_intersecting_circles_linear(primes_to_plot_extended, ax)
plt.title("Intersecting Circles for First 50 Primes (Linear Scaling)", fontsize=30)
plt.show()
