import numpy as np
import matplotlib.pyplot as plt

def generate_integers(n):
    return list(range(2, n + 2))

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def determine_color_and_marker(n, only_primes, only_composites):
    if only_primes and not is_prime(n):
        return None, None, None
    if only_composites and is_prime(n):
        return None, None, None
    if not is_prime(n):
        return 'black', 's', node_size_composite  # s for square marker
    color_map = {2: 'red', 4: 'orange', 6: 'yellow', 8: 'green', 10: 'blue'}  # add more if needed
    for separation, color in color_map.items():
        if is_prime(n + separation) or is_prime(n - separation):
            return color, 'o', node_size_prime  # o for circle marker
    return 'purple', 'o', node_size_prime

def plot_intersecting_circles(integers, ax, only_primes=False, only_composites=False):
    max_integer = max(integers)

    for idx, integer in enumerate(integers):
        angles = np.linspace(0, 2 * np.pi, integer, endpoint=False)
        radius = idx + 2  # Use linear scaling for radii
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        circle = plt.Circle((0, 0), radius, color='lightgray', fill=False)
        ax.add_artist(circle)
        color, marker, node_size = determine_color_and_marker(integer, only_primes, only_composites)
        if color is not None:
            ax.scatter(x, y, s=node_size, color=color, marker=marker)

    max_radius = len(integers) + 1
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_aspect('equal')
    ax.axis('off')

node_size_prime = 20  # you can adjust this to change the size of the dots representing primes
node_size_composite = 10  # you can adjust this to change the size of the dots representing composites

integers_to_plot_extended = generate_integers(300)
fig, ax = plt.subplots(figsize=(20, 20))
plot_intersecting_circles(integers_to_plot_extended, ax, only_primes=True)  # set only_primes or only_composites to True as needed
plt.title("RNS Integers", fontsize=30)
plt.savefig("integers.jpg", dpi=400)
plt.show()
