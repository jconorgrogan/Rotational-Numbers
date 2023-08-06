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

def determine_color_and_marker(n):
    if not is_prime(n):
        return 'black', 's'  # s for square marker
    color_map = {2: 'red', 4: 'orange', 6: 'yellow', 8: 'green', 10: 'blue'}  # add more if needed
    for separation, color in color_map.items():
        if is_prime(n + separation) or is_prime(n - separation):
            return color, 'o'  # o for circle marker
    return 'purple', 'o'

def plot_intersecting_circles(integers, ax):
    max_integer = max(integers)
    node_size_prime = 4
    node_size_composite = 2

    for idx, integer in enumerate(integers):
        angles = np.linspace(0, 2 * np.pi, integer, endpoint=False)
        radius = idx + 2  # Use linear scaling for radii
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        circle = plt.Circle((0, 0), radius, color='lightgray', fill=False)
        ax.add_artist(circle)
        color, marker = determine_color_and_marker(integer)
        node_size = node_size_prime if marker == 'o' else node_size_composite
        ax.scatter(x, y, s=node_size, color=color, marker=marker)

    max_radius = len(integers) + 1
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_aspect('equal')
    ax.axis('off')

integers_to_plot_extended = generate_integers(500)
fig, ax = plt.subplots(figsize=(40, 40))
plot_intersecting_circles(integers_to_plot_extended, ax)
plt.title("RNS Integers", fontsize=30)
plt.savefig("integers.jpg", dpi=800)
plt.show()
