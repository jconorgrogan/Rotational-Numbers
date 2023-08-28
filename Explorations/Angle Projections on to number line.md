# Geometric Analysis of Intersections

## Background

We analyzed the relationship between intersections on a projected line and the points on a unit circle. 
The unit circle is divided into equidistant nodes based on an angle \( \\theta \), which is calculated as:

\[ \\theta = \\frac{{2\\pi}}{{n}} \]

## Geometric Interpretation

As \( n \) increases, the angle \( \\theta \) decreases, leading to the following geometric implications:

1. **Decreasing Angles**: The angle between successive nodes on the unit circle decreases.
2. **Increasing Projection Angles**: The angle \( \\alpha = \\pi - \\theta \) of the projection line with the horizontal axis increases.
3. **Increasing Intersection Points**: The x-coordinate of the intersection with the horizontal line increases.

## Derived Equation

The x-coordinate of the intersection point is given by:

\`\`\`
x_intersection = \\frac{{\\sin(\\theta)}}{{\\cos(\\theta) + \\tan(\\alpha)}}
\`\`\`

This equation encapsulates the geometric relationship between the angles and the sides of the triangles formed in this construction.
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/55bd3b32-a994-4317-9904-e300894b23c0)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_green_lines_projection_n2_to_n15():
    projection_length = 1
    intersection_points = []
    for n in range(2, 16):
        angle_n = 2 * np.pi - (2 * np.pi / n)
        angle_n = angle_n if angle_n <= np.pi / 2 else angle_n - 2 * np.pi
        x_n = np.cos(angle_n) * projection_length
        y_n = np.sin(angle_n) * projection_length
        
        if n == 2:
            intersect_x = 0
        elif x_n != 0:
            slope_n = y_n / x_n
            intersect_x = -1 / slope_n
        else:
            intersect_x = 0
        
        plt.plot([0, intersect_x], [0, -1], 'g-', lw=0.5)
        plt.plot(intersect_x, -1, 'ro')
        plt.text(intersect_x, -1, f'({intersect_x:.2f}, -1)', fontsize=8)
        intersection_points.append((n, intersect_x, -1))
    return intersection_points

plt.figure(figsize=(10, 10))
plt.plot(np.cos(np.linspace(0, 2 * np.pi, 1000)), np.sin(np.linspace(0, 2 * np.pi, 1000)), 'k-')
intersection_points_n2_to_n15_extended = plot_green_lines_projection_n2_to_n15()
plt.axhline(-1, color='blue', lw=1)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.axis('equal')
plt.axis('off')
plt.title('Green lines projection for n = 2 to n = 15 with intersections (extended lines)')
plt.show()

intersection_table = pd.DataFrame(intersection_points_n2_to_n15_extended, columns=['n', 'x-coordinate', 'y-coordinate'])
intersection_table.set_index('n', inplace=True)
