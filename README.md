
## 1. Introduction

<img width="695" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/3a63e736-12a0-4d6c-8e6c-c41dc7991e91">

## 2. Positional Representation in ENT

In the Equidistant Number Theory (ENT), each natural number `n` is depicted by `n` equidistant nodes on a unit circle. The position of a node representing the `k`-th number is determined by the angle:

\[ \theta_k = \frac{2\pi(k-1)}{n} \]

The subtraction of 1 ensures that the first number in the sequence starts at \(0\) radians or degrees.

## 3. Prime and Factor Identification via Rotational Overlap

Given a set of `N` nodes, each node `k` has an associated angle:

\[ \theta_k = \frac{2\pi(k-1)}{N} \]

On rotating each node by its respective angle, no two nodes will overlap with the starting positions of any nodes throughout a full rotation unless a divisor relationship exists between them.

This geometric representation leads to an intuitive method for discerning prime numbers and factorizing composites.

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


### 4. Connection to Euler's formula 
The Rotational Number System (RNS) reinterprets mathematical operations and the relationships between numbers from a geometric perspective, with a particular emphasis on the role of 
�
π as a half-rotation or negation operation.

In the RNS, multiplication is seen as a rotation in the complex plane. Specifically, multiplying a complex number by a factor of the form 
�
�
�
e 
iθ
  corresponds to a rotation of the number by an angle of 
�
θ in the complex plane. For example, multiplication by 
�
=
�
�
�
2
i=e 
i 
2
π
​
 
  represents a quarter-turn or 
�
2
2
π
​
  (90°) rotation.

The reinterpretation of 
�
π as -1 is a key aspect of the RNS. This idea is derived from considering 
�
π as a half-rotation or 
18
0
∘
180 
∘
  operation. Thus, multiplying a number by a factor of 
�
π is equivalent to flipping the number to its opposite point on the unit circle. In other words, 
�
π and -1 are intrinsically linked in this system, leading to a deep connection between the geometric operation of rotation and the algebraic operation of negation.

This connection also results in a significant transformation of trigonometric identities in the RNS. With 
�
π signifying -1, the identities for sine and cosine functions become reflections about the y-axis post-
�
π:

sin
⁡
(
�
+
�
)
=
−
sin
⁡
(
�
)
sin(π+θ)=−sin(θ)
cos
⁡
(
�
+
�
)
=
−
cos
⁡
(
�
)
cos(π+θ)=−cos(θ)
Furthermore, in the RNS, 
�
π is no longer a transcendental number but is redefined as -1, an algebraic entity. This blurs the traditional boundaries between algebraic and transcendental numbers, potentially leading to new classifications and properties of numbers.

Euler's formula 
�
�
�
+
1
=
0
e 
iπ
 +1=0 also takes on a new meaning in the RNS. It states that a half-turn rotation (i.e., exponentiating with 
�
�
πi) from 1 leads to -1. In this way, Euler's formula encapsulates the essence of the RNS, emphasizing the fundamental role of rotations and positions on the unit circle.

The Fourier Transform in the RNS context offers an alternative perspective on frequency components and signal processing. The exponential term 
�
−
�
�
�
�
e 
−iπωt
  is viewed not just as a complex sinusoid but as a continuous series of rotations and negations.

Finally, the intrinsic link between 
�
π and -1 in the RNS suggests a new perspective on the nature of the universe. It implies that cyclicity, return, and opposition are fundamental to the nature of the universe, leading to a worldview where cycles and oppositions are not just patterns but fundamental truths.

## Euler's Formula:

Traditionally, Euler's formula is expressed as:
\[ e^{ix} = \cos(x) + i\sin(x) \]
Here, exponentiating with a complex number results in a combination of trigonometric functions.

### Imaginary Unit, \( i \):

The imaginary unit \( i \) is defined as:
\[ i^2 = -1 \]
In the ENT context, multiplication by \( i \) represents a quarter-turn or 90° rotation, transitioning from the real to the imaginary dimension. This captures the essence of:
\[ e^{i\frac{\pi}{2}} = i \]
Exponentiating with a complex quarter-turn (i.e., \( \frac{\pi}{2} \)) results in a transition to the imaginary axis.

### Euler's Number, \( e \):

Euler's number \( e \) represents continuous growth or decay. In the ENT, \( e \) can be visualized as a continuous, compounded transformation. When combined with the \( i\pi \) rotation, it leads to cyclical behaviors and a standing wave:
\[ e^{i\pi} = -1 \]

### Complex Plane Dynamics:

In the complex plane, multiplication by a complex number typically involves both rotation and dilation. In the ENT, with \( \pi = -1 \), this multiplication becomes purely a rotation, specifically a half-turn. This offers a more unified perspective on complex multiplication, with \( \pi \) serving as a fundamental pivot.

### Algebraic-Geometric Interplay:

Given \( \pi \) as \( -1 \), multiplication in the ENT is inherently a geometric operation. For any real number \( x \):
\[ x \times \pi = -x \]
This equation dictates that multiplication by \( \pi \) algebraically negates \( x \), while geometrically, it rotates \( x \) by \( \pi \) radians on the unit circle, a half-rotation. Thus, the algebraic operation of negation is intertwined with the geometric operation of rotation.

### ENT-Based Trigonometry:

With \( \pi \) signifying \( -1 \), trigonometric identities undergo transformation:

For any angle \( \theta \):
\[ \sin(\pi + \theta) = -\sin(\theta) \]
\[ \cos(\pi + \theta) = -\cos(\theta) \]
These equations suggest that trigonometric functions post-\( \pi \) are reflections of their pre-\( \pi \) values, emphasizing the duality inherent to \( \pi \) in the ENT.

### Representation in the Complex Plane

Every term in the Fourier series can be represented as a complex number using Euler's formula:

\[ e^{i\theta} = \cos(\theta) + i \sin(\theta) \]

So, the terms in the Fourier series become:

\[ f(t) = a_0 + \sum_{n=1}^{\infty} r_n e^{i(2\pi n f t + \phi_n)} \]

where \( r_n = \sqrt{a_n^2 + b_n^2} \) represents the magnitude and \( \phi_n = \arctan\left(\frac{b_n}{a_n}\right) \) is the phase.

Each term \( r_n e^{i(2\pi n f t + \phi_n)} \) corresponds to a point in the complex plane, represented by its magnitude \( r_n \) and its phase \( \phi_n \). In the ENT, this point would be visualized as a rotation around the origin, with a radius of \( r_n \) and an angle of \( \phi_n \).

### Waveform Compression

The ENT can be linked to wave properties using the Fourier series. Given a wave function \( f(t) \), its Fourier series is:

\[ f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(2\pi n f t) + b_n \sin(2\pi n f t) \right] \]

In the ENT, each term in this series can correspond to a number's rotational representation. This perspective allows for wave operations to be intuitively understood as transformations in the ENT.

By extending this concept further, it's theoretically possible to encode more complex data, such as a piece of music, as a set of integers. 
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/8e9b6e96-5dad-43d8-bc64-89640e0c4b8b)

