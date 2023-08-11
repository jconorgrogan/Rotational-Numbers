import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.animation as animation

def theta(k, n):
    return 2 * np.pi * (k - 1) / n

def draw_single_circle(n, m, rotation=0):
    angles_n = [theta(k, n) for k in range(1, n + 1)]
    angles_m = [(theta(k, m) + rotation) % (2 * np.pi) for k in range(1, m + 1)]
    x_n = [np.cos(angle) for angle in angles_n]
    y_n = [np.sin(angle) for angle in angles_n]
    x_m = [np.cos(angle) for angle in angles_m]
    y_m = [np.sin(angle) for angle in angles_m]
    return x_n, y_n, x_m, y_m

tolerance = 0.05

def calculate_overlaps(n, m, rotation):
    overlaps = []
    angles_n = [theta(k, n) for k in range(1, n + 1)]
    angles_m = [(theta(k, m) + rotation) % (2 * np.pi) for k in range(1, m + 1)]
    for angle_n in angles_n:
        for angle_m in angles_m:
            if abs(angle_n - angle_m) < tolerance:
                overlaps.append((np.cos(angle_n), np.sin(angle_n)))
    return overlaps

overlap_lines = []

def draw_lines_for_overlap(ax, overlaps):
    global overlap_lines
    if overlaps:
        center = (0, 0)
        for overlap in overlaps:
            line = Line2D([center[0], overlap[0]], [center[1], overlap[1]], color='green')
            overlap_lines.append(line)
            ax.add_line(line)

    for line in overlap_lines:
        ax.add_line(line)

def update_prettier(val):
    rotation_angle = val
    ax.clear()
    x_n, y_n, x_m, y_m = draw_single_circle(n, m, rotation=rotation_angle)
    ax.scatter(x_n, y_n, color='red', marker='o', s=50, label='n-points')
    ax.scatter(x_m, y_m, color='blue', marker='x', s=50, label='m-points (rotatable)')
    overlaps = calculate_overlaps(n, m, rotation_angle)
    for overlap in overlaps:
        ax.scatter(*overlap, color='green', marker='*', s=150 if len(overlaps) >= 2 else 100, zorder=5)
    draw_lines_for_overlap(ax, overlaps)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.add_artist(plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--'))
    ax.legend(loc='upper right', fontsize=8)
    plt.draw()

def animate(frame):
    global previous_frame
    rotation_angle = (frame * 2 * np.pi / 200) % (2 * np.pi)
    slider.set_val(rotation_angle)
    update_prettier(rotation_angle)
    previous_frame = frame

n = 21
m = 3

fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.1, bottom=0.35)

x_n, y_n, x_m, y_m = draw_single_circle(n, m)
ax.scatter(x_n, y_n, color='red', marker='o', s=50)
ax.scatter(x_m, y_m, color='blue', marker='x', s=50)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.add_artist(plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--'))

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Rotation', 0, 2 * np.pi, valinit=0)
slider.on_changed(update_prettier)

previous_frame = 0
ani = animation.FuncAnimation(fig, animate, frames=200, repeat=True, interval=100)

plt.show()
