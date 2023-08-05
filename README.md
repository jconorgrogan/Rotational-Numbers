# Rotational Number Theory

# Rotational Number Theory

## 1. Introduction

The Rotational Number System (RNS) offers a novel visualization of numbers in a circular construct. This system represents each natural number \( n \) as \( n \) equidistant nodes positioned on a circle. The objective is to redefine mathematical operations in this rotational context and draw parallels with existing mathematical constructs.

## 2. Rotational Identity

Given a natural number \( n \), its rotational identity in the RNS is defined by its representation on the unit circle in the complex plane. Mathematically, this is expressed as:

\[ R(n) = e^{\frac{2\pi i}{n}} \]

This equation yields a root of unity for every natural number.

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

