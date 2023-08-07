
## 1. Introduction

In the Equidistant Number Theory (ENT), each natural number `n` is depicted by `n` equidistant nodes on a unit circle. 

![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/d94798c6-aa7c-4ece-84b2-6a17fab5192b)


The position of a node representing the `k`-th number is determined by the angle:

\[ \theta_k = \frac{2\pi(k-1)}{n} \]

The subtraction of 1 ensures that the first number in the sequence starts at \(0\) radians or degrees.

## 2. Prime and Factor Identification via Rotational Overlap

On rotating each node by its respective angle, no two nodes will overlap with the starting positions of any nodes throughout a full rotation unless a divisor relationship exists between them.

This geometric representation leads to an intuitive method for discerning prime numbers and factorizing composites.



## 3. Operations in ENT

The following operators (which have a lot of connection with signal processing) are used in ENT:
| Operator       | Mathematical Basis         | Effect on Nodes | Core Mathematical Components  | DSP Connection      |
| -------------- | -------------------------- | --------------- | ----------------------------- | ------------------- |
| Addition       | Appending new nodes        | Addition of new nodes and recalibration to maintain equidistance | theta(n) = 2pi(n-1) / (n+a) | Superposition Principle |
| Subtraction    | Removal of existing nodes  | Removal of nodes and recalibration to maintain equidistance | theta(n) = 2pi(n-1) / (n-a) | Wave Cancellation (Destructive Interference) |
| Multiplication | Creating copies of the nodes and redistributing them around the circle | Repetition of nodes based on the multiplication factor; each copy rotated by an angle relative to the previous copy | theta(n, k) = 2pi(n-1) / a + 2pi(k-1) / b | Frequency Modulation |
| Division       | Inverse of multiplication  | Redistribution of nodes based on the division factor; each copy rotated by an angle relative to the previous copy | theta(n, k) = 2pi(n-1) / a - 2pi(k-1) / b | Frequency Demodulation |
| Fraction (Decimal) | Partial completion of circle | Placement of nodes less than a full circle | theta(n) = 2pi(n-1) / (n+alpha) (where alpha < 1) | Phase Modulation |
| Negation       | Flipping of the nodes      | Nodes flipped across the origin | theta(n) = -2pi(n-1) / n | Wave Inversion (180 Degree Phase Shift) |
| Absolute value | Absolute value of nodes    | All nodes moved to the positive half | theta(n) = abs(2pi(n-1) / n) | Rectification (All Positive Wave) |
| Exponentiation | Spiral formation           | Nodes are placed in an expanding spiral pattern | theta(n) = r^(n-1)e^(2pi i(n-1)/n) | Amplitude Modulation |
| Logarithm      | Inverse spiral formation   | Nodes are placed in a contracting spiral pattern | theta(n) = log(r^(n-1))e^(2pi i(n-1)/n) | Signal Compression |
| Modulo         | Folding back of nodes      | Nodes beyond the modulo number are folded back | theta(n) = 2pi((n-1) mod m) / m | Wave Wrapping (Overflow Handling) |


RNS offers a geometric perspective on the relationships between numbers and mathematical operations

In the RNS, multiplication is understood as a rotation in the complex plane. Specifically, multiplying a complex number by a factor of the form e^(iθ) corresponds to rotating the number by an angle of θ in the complex plane. For instance, multiplication by 2i = e^(i(2π)) represents a quarter-turn or 90° rotation.

Here, π signifies a half-rotation or 180° operation. Therefore, multiplying a number by π equates to flipping the number to its opposite point on the unit circle. In this context, π and -1 are intimately connected in this system, establishing a profound link between the geometric operation of rotation and the algebraic operation of negation.

This association also leads to a significant transformation of trigonometric identities in the RNS. With π signifying a half-rotation, the identities for sine and cosine functions are as follows:

sin(π + θ) = -sin(θ)
cos(π + θ) = -cos(θ)

This is essentially due to the periodic nature of these functions, with a period of 2π.

Euler's formula e^(iπ) + 1 = 0 takes on a novel meaning in the RNS. It asserts that a half-turn rotation (exponentiating with πi) from 1 leads to -1. This formula embodies the essence of the RNS, accentuating the vital role of rotations and positions on the unit circle.

In the context of the Fourier Transform, the exponential term e^(-iπωt) is not merely a complex sinusoid but a continuous series of rotations and negations. This viewpoint presents an alternative understanding of frequency components and signal processing.

## Euler's Formula:

Traditionally, Euler's formula is expressed as:
e^{ix} = cos(x) + isin(x)
Here, exponentiating with a complex number results in a combination of trigonometric functions.

Imaginary Unit, 
�
i:
The imaginary unit i is defined as:
i^2 = -1
In the RNS, multiplication by i signifies a quarter-turn or 90° rotation, transitioning from the real to the imaginary dimension. This captures the essence of:
e^{i(π/2)} = i
Exponentiating with a complex quarter-turn (i.e., (π/2)) results in a transition to the imaginary axis.

Euler's number e embodies continuous growth or decay. In the RNS, e can be visualized as a continuous, compounded transformation. When combined with the iπ rotation, it leads to cyclical behaviors and a standing wave:

e^{iπ} = -1

Complex Plane Dynamics:
In the complex plane, multiplication by a complex number typically involves both rotation and dilation. In the RNS, with π = -1, this multiplication becomes purely a rotation, specifically a half-turn. This offers a more unified perspective on complex multiplication, with π serving as a fundamental pivot.

Algebraic-Geometric Interplay:
Given π as -1, multiplication in the RNS is inherently a geometric operation. For any real number x:

x × π = -x
This equation stipulates that multiplication by π algebraically negates x, while geometrically, it rotates x by π radians on the unit circle, a half-rotation. Thus, the algebraic operation of negation is intertwined with the geometric operation of rotation.

RNS-Based Trigonometry:
With π signifying -1, trigonometric identities undergo transformation:

For any angle θ:
sin(π + θ) = -sin(θ)
cos(π + θ) = -cos(θ)
These equations suggest that trigonometric functions post-π are reflections of their pre-π values, emphasizing the duality inherent to π in the RNS.

Every term in the Fourier series can be represented as a complex number using Euler's formula:

e^{iθ} = cos(θ) + isin(θ)
So, the terms in the Fourier series become:
f(t) = a_0 + ∑_{n=1}^{∞} r_n e^{i(2πnf t + φ_n)}
where r_n = sqrt(a_n^2 + b_n^2) represents the magnitude and φ_n = arctan(b_n/a_n) is the phase.

Each term r_n e^{i(2πnf t + φ_n)} corresponds to a point in the complex plane, represented by its magnitude r_n and its phase φ_n. In the RNS, this point would be visualized as a rotation around the origin, with a radius of r_n and an angle of φ_n.

### Waveform Compression

The ENT can be linked to wave properties using the Fourier series. Given a wave function \( f(t) \), its Fourier series is:

\[ f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(2\pi n f t) + b_n \sin(2\pi n f t) \right] \]

In the ENT, each term in this series can correspond to a number's rotational representation. This perspective allows for wave operations to be intuitively understood as transformations in the ENT.

By extending this concept further, it's theoretically possible to encode more complex data, such as a piece of music, as a set of integers. 
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/8e9b6e96-5dad-43d8-bc64-89640e0c4b8b)

