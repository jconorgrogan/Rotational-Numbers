from matplotlib.collections import LineCollection
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def theta(k, n):
    return 2 * np.pi * (k - 1) / n

def draw_concentric_circles(rotation_angles):
    lines = []
    for i in range(2, max_number + 1):
        angles = np.linspace(0, 2 * np.pi, i, endpoint=False)
        rotation = rotation_angles[i - 2] if i % 2 == 0 else -rotation_angles[i - 2]
        x = np.cos(angles + rotation) * i
        y = np.sin(angles + rotation) * i
        ax.scatter(x, y, marker='o', s=50)
        ax.add_artist(plt.Circle((0, 0), i, color='black', fill=False, linestyle='--'))
        
        # Check for overlaps
        for j in range(i+1, max_number + 1):
            overlap_angles = np.linspace(0, 2 * np.pi, j, endpoint=False)
            overlap_rotation = rotation_angles[j - 2] if j % 2 == 0 else -rotation_angles[j - 2]
            overlap_x = np.cos(overlap_angles + overlap_rotation) * j
            overlap_y = np.sin(overlap_angles + overlap_rotation) * j
            
            for xi, yi in zip(x, y):
                for xj, yj in zip(overlap_x, overlap_y):
                    if abs(xi - xj) < tolerance and abs(yi - yj) < tolerance:
                        lines.append([(xi, yi), (xj, yj)])

    # Draw all lines
    lc = LineCollection(lines, colors=cm.rainbow(np.linspace(0, 1, len(lines))), linestyle='--')
    ax.add_collection(lc)
    return ax.collections + ax.lines + ax.patches

def animate_concentric(frame):
    rotation_angles = [frame * 2 * np.pi / 200] * (max_number - 1) # Same rotation angle for all circles
    ax.clear()
    return draw_concentric_circles(rotation_angles)

tolerance = 0.05
max_number = 25 # Change this value to include more or fewer concentric circles

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(left=0.1, bottom=0.35)
ax.set_aspect('equal')
ax.set_xlim(-max_number - 1, max_number + 1)
ax.set_ylim(-max_number - 1, max_number + 1)

ani_concentric = animation.FuncAnimation(fig, animate_concentric, frames=200, repeat=True, interval=200, blit=True) # Enable blitting

plt.show()
