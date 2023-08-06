

## 1. Introduction

The Rotational Number System (RNS) provides a unique circular representation for natural numbers. In RNS, each natural number \( n \) is depicted by a specific node on a circle, with all numbers being equidistant from each other. The objective is to explore mathematical operations within this rotational framework and draw analogies with traditional mathematical systems.

## 2. Positional Representation in RNS

Every natural number \( n \) is assigned a unique position on the unit circle. The position of the number \( n \) is determined by dividing the circle into \( n \) equidistant nodes. The position is given by the angle:

\[ \theta(n) = \frac{2\pi(n-1)}{N} \]

Where \( N \) is the maximum number to be represented on the circle. The subtracting 1 ensures that the number 1 starts from \( 0 \) degrees or radians.


**Observations**:
- For primes, the roots of unity are trivial (i.e., 1 and -1) until \( n \) is reached.
- For composites, some roots of unity will align before \( n \) is reached, which corresponds to the factors of \( n \).

## 3. Waves and the Rotational Number System

The RNS can be linked to wave properties using the Fourier series. Given a wave function \( f(t) \), its Fourier series is:

\[ f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(2\pi n f t) + b_n \sin(2\pi n f t) \right] \]

In the RNS, each term in this series can correspond to a number's rotational representation. This perspective allows for wave operations to be intuitively understood as transformations in the RNS.

## 4. Euler's Identity in the RNS

Euler's identity is given by:

\[ e^{i\pi} + 1 = 0 \]

This can be visualized in the RNS as:
- Begin at the point representing the number 1 on the unit circle.
- Rotate by \( \pi \) radians to reach the point representing -1.
- Adding 1 brings us back to the origin.

## 5. Implications and Potential Applications

- **Factorization**: The rotational identity of composite numbers can hint at their factors. For example, if a number aligns halfway through a rotation, it indicates divisibility by 2.
- **Number Theory**: Unique rotational patterns might emerge when studying number theoretic functions in the RNS.
- **Higher Dimensions**: Complex numbers can be visualized in a 3D RNS, with an added dimension for the imaginary part. Extensions like quaternions could lead to even higher-dimensional representations.
- **Dynamical Systems**: The state and evolution of dynamical systems can be visualized in the RNS, offering new insights into system behaviors.

### Representation in the Complex Plane

Every term in the Fourier series can be represented as a complex number using Euler's formula:

\[ e^{i\theta} = \cos(\theta) + i \sin(\theta) \]

So, the terms in the Fourier series become:

\[ f(t) = a_0 + \sum_{n=1}^{\infty} r_n e^{i(2\pi n f t + \phi_n)} \]

where \( r_n = \sqrt{a_n^2 + b_n^2} \) represents the magnitude and \( \phi_n = \arctan\left(\frac{b_n}{a_n}\right) \) is the phase.

Each term \( r_n e^{i(2\pi n f t + \phi_n)} \) corresponds to a point in the complex plane, represented by its magnitude \( r_n \) and its phase \( \phi_n \). In the RNS, this point would be visualized as a rotation around the origin, with a radius of \( r_n \) and an angle of \( \phi_n \).



| Operator | Mathematical Basis | Effect on Nodes | Effect on Wave | Core Mathematical Components |
|:--------:|:------------------:|:---------------:|:--------------:|:-----------------------------:|
| Addition | Appending new nodes | Addition of new nodes and recalibration to maintain equidistance | Superposition of new wave | `theta(n) = 2pi(n-1) / (n+a)` |
| Subtraction | Removal of existing nodes | Removal of nodes and recalibration to maintain equidistance | Cancellation of the corresponding wave | `theta(n) = 2pi(n-1) / (n-a)` |
| Multiplication | Creating copies of the nodes and redistributing them around the circle | Repetition of nodes based on the multiplication factor; each copy rotated by an angle relative to the previous copy | Frequency modulation | `theta(n, k) = 2pi(n-1) / a + 2pi(k-1) / b` |
| Division | Inverse of multiplication | Redistribution of nodes based on the division factor; each copy rotated by an angle relative to the previous copy | Frequency demodulation | `theta(n, k) = 2pi(n-1) / a - 2pi(k-1) / b` |
| Fraction (Decimal) | Partial completion of circle | Placement of nodes less than a full circle | Phase modulation | `theta(n) = 2pi(n-1) / (n+alpha)` (where `alpha < 1`) |
| Negation | Flipping of the nodes | Nodes flipped across the origin | Wave inversion (180 degree phase shift) | `theta(n) = -2pi(n-1) / n` |
| Absolute value | Absolute value of nodes | All nodes moved to the positive half | Rectification (all positive wave) | `theta(n) = abs(2pi(n-1) / n)` |
| Exponentiation | Spiral formation | Nodes are placed in an expanding spiral pattern | Progressive increase in frequency and amplitude | `theta(n) = r^(n-1)e^(2pi i(n-1)/n)` |
| Logarithm | Inverse spiral formation | Nodes are placed in a contracting spiral pattern | Progressive decrease in frequency and amplitude | `theta(n) = log(r^(n-1))e^(2pi i(n-1)/n)` |
| Modulo | Folding back of nodes | Nodes beyond the modulo number are folded back | Wave wrapping at a specific frequency | `theta(n) = 2pi((n-1) mod m) / m` |

$$### Representation in the Complex Plane

Each term in a Fourier series can be represented as a complex number leveraging Euler's formula:

$$ e^{i\theta} = \cos(\theta) + i \sin(\theta) $$

Thus, the Fourier series representation becomes:

$$ f(t) = a_0 + \sum_{n=1}^{\infty} r_n e^{i(2\pi n f t + \phi_n)} $$

Here, the magnitude \( r_n = \sqrt{a_n^2 + b_n^2} \) and the phase \( \phi_n = \arctan\left(\frac{b_n}{a_n}\right) \) define the position of each term \( r_n e^{i(2\pi n f t + \phi_n)} \) in the complex plane. In the RNS, this term is visualized as a rotation around the origin with radius \( r_n \) and angle \( \phi_n \). The concept of RNS presents a compelling way to visualize the operations involved in Fourier analysis.


