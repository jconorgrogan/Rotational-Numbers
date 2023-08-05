

## 1. Introduction

The Rotational Number System (RNS) provides a unique circular representation for natural numbers. In RNS, each natural number \( n \) is depicted by a specific node on a circle, with all numbers being equidistant from each other. The objective is to explore mathematical operations within this rotational framework and draw analogies with traditional mathematical systems.

## 2. Positional Representation in RNS

Every natural number \( n \) is assigned a unique position on the unit circle. The position of the number \( n \) is determined by dividing the circle into \( n \) equidistant nodes. The position is given by the angle:

\[ \theta(n) = \frac{2\pi(n-1)}{N} \]

Where \( N \) is the maximum number to be represented on the circle. The subtracting 1 ensures that the number 1 starts from \( 0 \) degrees or radians.

## 3. Rotational Identity

The rotational identity of a number in the RNS is its representation on the unit circle in the complex plane:

\[ R(n) = e^{\frac{2\pi i (n-1)}{N}} \]

This formula provides a root of unity for every natural number.


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

### Wave Compression using the RNS

When representing a wave as a sum of its Fourier components, many of these components might have negligible magnitudes. In the RNS, these negligible components would correspond to points very close to the origin.

- **Sparse Representation**: Given the circular visualization in the RNS, it's intuitive to identify and discard the components that have negligible magnitude, as they contribute minimally to the overall wave. This results in a sparse representation, retaining only the significant components.
- **Quantization**: By grouping nearby points in the RNS, we can quantize the representation space. Instead of representing each point precisely, points that are close to each other can be represented by a common value. This further compresses the wave representation.
- **Efficient Storage**: The RNS representation can be stored using two arrays: one for the significant magnitudes and another for the associated phases. By discarding negligible components and using quantization, the size of these arrays can be significantly reduced.
- **Reconstruction**: Despite the compression, the wave can be reconstructed with high fidelity by summing up the retained Fourier components. The RNS ensures that the compressed representation captures the most significant features of the wave.

  | Operator | Mathematical Basis | Effect on Nodes | Effect on Wave | Core Mathematical Components |
|:--------:|:------------------:|:---------------:|:--------------:|:-----------------------------:|
| Addition | Appending new nodes | Addition of new nodes and recalibration to maintain equidistance | Superposition of new wave | \( \theta(n) = \frac{2\pi(n-1)}{n+a} \) |
| Subtraction | Removal of existing nodes | Removal of nodes and recalibration to maintain equidistance | Cancellation of the corresponding wave | \( \theta(n) = \frac{2\pi(n-1)}{n-a} \) |
| Multiplication | Creating copies of the nodes and redistributing them around the circle | Repetition of nodes based on the multiplication factor; each copy rotated by an angle relative to the previous copy | Frequency modulation | \( \theta(n, k) = \frac{2\pi(n-1)}{a} + \frac{2\pi(k-1)}{b} \) |
| Division | Inverse of multiplication | Redistribution of nodes based on the division factor; each copy rotated by an angle relative to the previous copy | Frequency demodulation | \( \theta(n, k) = \frac{2\pi(n-1)}{a} - \frac{2\pi(k-1)}{b} \) |
| Fraction (Decimal) | Partial completion of circle | Placement of nodes less than a full circle | Phase modulation | \( \theta(n) = \frac{2\pi(n-1)}{n+\alpha} \) (where \( \alpha < 1 \)) |
| Negation | Flipping of the nodes | Nodes flipped across the origin | Wave inversion (180 degree phase shift) | \( \theta(n) = -\frac{2\pi(n-1)}{n} \) |
| Absolute value | Absolute value of nodes | All nodes moved to the positive half | Rectification (all positive wave) | \( \theta(n) = |\frac{2\pi(n-1)}{n}| \) |
| Exponentiation | Spiral formation | Nodes are placed in an expanding spiral pattern | Progressive increase in frequency and amplitude | \( \theta(n) = r^{(n-1)}e^{2\pi i(n-1)/n} \) |
| Logarithm | Inverse spiral formation | Nodes are placed in a contracting spiral pattern | Progressive decrease in frequency and amplitude | \( \theta(n) = \log(r^{(n-1)})e^{2\pi i(n-1)/n} \) |
| Modulo | Folding back of nodes | Nodes beyond the modulo number are folded back | Wave wrapping at a specific frequency | \( \theta(n) = \frac{2\pi((n-1) \mod m)}{m} \) |

$$### Representation in the Complex Plane

Each term in a Fourier series can be represented as a complex number leveraging Euler's formula:

$$ e^{i\theta} = \cos(\theta) + i \sin(\theta) $$

Thus, the Fourier series representation becomes:

$$ f(t) = a_0 + \sum_{n=1}^{\infty} r_n e^{i(2\pi n f t + \phi_n)} $$

Here, the magnitude \( r_n = \sqrt{a_n^2 + b_n^2} \) and the phase \( \phi_n = \arctan\left(\frac{b_n}{a_n}\right) \) define the position of each term \( r_n e^{i(2\pi n f t + \phi_n)} \) in the complex plane. In the RNS, this term is visualized as a rotation around the origin with radius \( r_n \) and angle \( \phi_n \). The concept of RNS presents a compelling way to visualize the operations involved in Fourier analysis.

### Wave Compression using the RNS

While representing a wave as a sum of its Fourier components, many components might have negligible magnitudes. These components correspond to nodes very close to the origin in the RNS.

- **Sparse Representation**: The circular visualization in the RNS allows for an intuitive approach to identify and discard components that contribute minimally to the overall wave. This results in a sparse representation, retaining only the significant components. Hence, RNS offers a clear and efficient way to compress data.

- **Quantization**: Grouping nearby nodes in the RNS permits a form of quantization of the representation space. Instead of precisely representing each node, nodes that are close to each other can be represented by a common value, thereby compressing the wave representation even further.

- **Efficient Storage**: The RNS representation can be stored efficiently using two arrays: one for the significant magnitudes and another for the corresponding phases. The size of these arrays can be significantly reduced through the discarding of negligible components and the use of quantization.

- **Reconstruction**: The compressed wave representation can be reconstructed with high fidelity by summing up the retained Fourier components. The RNS ensures that even with compression, the wave representation captures the most significant features of the wave.

In essence, the use of RNS enhances the capability to manipulate and visualize waveforms in a more intuitive manner. The efficiency in representation and the ability to perform meaningful compression highlight the potential for broad application in wave analysis and data compression strategies.
$$
