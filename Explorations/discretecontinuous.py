//1. **Circle and Segment:** Consider a circle with radius \( r \) and a segment of length \( x \) where \( 0 \leq x \leq r \).
//2. **Folding the Segment:** Fold the segment onto the circle, creating a right triangle with hypotenuse \( r \), adjacent side \( x \), and opposite side \( \sqrt{r^2 - x^2} \).
//3. **Calculating the Angle:** The angle \( \theta \) in radians corresponding to the folded segment is given by
//   \[
 //  \theta = \arccos\left(\frac{x}{r}\right).
//   \]
//4. **Representing Any Angle:** Since \( x \) can be any value between \( 0 \) and \( r \), \( \theta \) can be any value between \( 0 \) and \( \pi \).


import matplotlib.pyplot as plt
import numpy as np

def draw_circle_and_compute_number_with_nodes(blue_line_end_x, radius):
    # Calculating the blue line's end point
    blue_line_end_y = np.sqrt(radius**2 - blue_line_end_x**2)
    
    # Draw the circle
    circle = plt.Circle((0, 0), radius, color='blue', fill=False)
    fig, ax = plt.subplots()
    ax.add_artist(circle)

    # Draw the line from the origin to the blue line's start point
    plt.plot([0, blue_line_end_x], [0, 0], 'r-')

    # Draw the blue line
    plt.plot([blue_line_end_x, blue_line_end_x], [0, blue_line_end_y], 'b-')

    # Calculate the angle in radians
    angle_radians = np.arctan2(blue_line_end_y, blue_line_end_x)

    # Calculate the natural number based on equidistant nodes
    natural_number = int(np.floor(2 * np.pi / angle_radians))

    # Draw equidistant nodes around the complete circle
    for i in range(natural_number):
        angle = i * 2 * np.pi / natural_number
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        plt.scatter(x, y, c='green', marker='x', s=100)

    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    return angle_radians, natural_number

# Example inputs
blue_line_end_x = 5
radius = 10

# Calling the function with the example inputs
radians, natural_number = draw_circle_and_compute_number_with_nodes(blue_line_end_x, radius)
print("Radians:", radians)
print("Natural Number:", natural_number)
