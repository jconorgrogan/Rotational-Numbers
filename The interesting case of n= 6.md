For a circle with radius \( R \) and \( n \) equally spaced nodes, the task is to find the values of \( n \) that allow the distance \( D \) between adjacent nodes to fit an integer number of times across the diameter of the circle. The distance \( D \) between adjacent nodes is given by:

\[ D = 2R \sin\left(\frac{\pi}{n}\right) \]

Conclusion:
The instances where the distance \( D \) between nodes fits as an integer multiple across the diameter of the circle are:

- \( n = 2 \): The distance \( D \) fits exactly 1 time across the diameter, dividing the circle into two equal parts.
- \( n = 6 \): The distance \( D \) fits exactly 2 times across the diameter, dividing the circle into six equal parts.
- \( n = \infty \): A more abstract concept, where the distance \( D \) fits an infinite number of times across the diameter, representing a continuum or infinite division.

The condition we're looking for is when the distance \( D \) between nodes fits as an integer multiple across the diameter. We have:

\[ D = 2R \sin\left(\frac{\pi}{n}\right) \times k = 2R \]

Simplifying, we get:

\[ \sin\left(\frac{\pi}{n}\right) = \frac{1}{k} \]

The sine function has a range between -1 and 1, so the only integer values of \( k \) that would make the equation valid are 1 and 2.

- For \( k = 1 \), we get \( \sin\left(\frac{\pi}{n}\right) = 1 \), which leads to \( n = 2 \).
- For \( k = 2 \), we get \( \sin\left(\frac{\pi}{n}\right) = \frac{1}{2} \), which leads to \( n = 6 \).

No other integer values for \( k \) will satisfy the equation, hence these are the only integer solutions for \( n \), besides the limit case of \( n = \infty \).
