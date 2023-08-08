
## 1. Introduction

Equidistant Number Theory (ENT) is an attempt to unify mathmatics (And a unique way to test primality and find prime factors!)  ENT offers a bijective mapping between number theory and geometry; For every mathematical operation or number, there's a unique geometrical representation. The ENT's ability to express operations as rotations in the complex plane directly connects to quantum phase shifts and intuitively helps visualize complex motions such as in quaternions. 

In the Equidistant Number Theory, each natural number `n` is depicted by `n` equidistant nodes on a unit circle. All of the other elements of mathmatics derive from this concept. 

![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/d94798c6-aa7c-4ece-84b2-6a17fab5192b)

The position of a node representing the `k`-th number is determined by the angle:

![equation](https://latex.codecogs.com/gif.latex?\theta_k&space;=&space;\frac{2\pi(k-1)}{n})

The subtraction of 1 ensures that the first number in the sequence starts at \(0\) radians or degrees.

Here is python code that uses this rotational technique to find prime factors https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/blob/main/PrimeCheckAndFactorization.py

## 2. Prime and Factor Identification via Rotational Overlap

On rotating each node by its respective angle, no two nodes will overlap with the starting positions of any nodes throughout a full rotation unless a divisor relationship exists between them.

This geometric representation leads to an intuitive method for discerning prime numbers and factorizing composites.

3 is a factor of 6. Notice that you can "fit" 2 equidisdant "3s" (after one rotation) in the number 6
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/8f04aa3c-5ee2-4f4a-b60c-ac3f1c119bc4)


2 is not a factor of 5. No shapes of 1<n<5 nodes can symmetrically fit in 5 after a full rotation. 5 is therefore prime
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/73a1a797-ec5e-425d-a7b3-c13ca8ea1a43)


## 3. Operations in ENT

![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/29b221f0-c7b1-48f9-bdf8-db6c8175d570)

RNS offers a geometric perspective on the relationships between numbers and mathematical operations

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


**The Complex Plane**

In the RNS, multiplication in the complex domain is visualized as a combination of rotation in the complex plane and movement along a helix. This helical interpretation offers a three-dimensional depth to the traditional two-dimensional complex plane, enhancing our understanding of operations involving imaginary components.

When a complex number is multiplied by a factor of the form ![equation](https://latex.codecogs.com/gif.latex?e^{i\theta}), it corresponds to a rotation of that number by an angle \(\theta\) in the complex plane. Thus, multiplying by ![equation](https://latex.codecogs.com/gif.latex?2i=e^{i(2\pi)}) represents a quarter-turn or 90° rotation, and due to the imaginary component, it also results in an upward movement along the helix's axis.

The term ![equation](https://latex.codecogs.com/gif.latex?\pi) represents a 180° operation or half-rotation. Multiplying by ![equation](https://latex.codecogs.com/gif.latex?\pi) reflects the number to its opposite point on the unit circle, illustrating the deep connection between geometric rotation and algebraic negation in this framework.

This structure modifies trigonometric identities within the RNS. With \(\pi\) signifying a half-rotation:
![equation1](https://latex.codecogs.com/gif.latex?sin(\pi&plus;\theta)=-sin(\theta))
![equation2](https://latex.codecogs.com/gif.latex?cos(\pi&plus;\theta)=-cos(\theta))

The periodicity of these functions, having a period of 2![equation](https://latex.codecogs.com/gif.latex?\pi), is an essential aspect.

Euler's formula ![equation3](https://latex.codecogs.com/gif.latex?e^{i\pi}&plus;1=0) gains a nuanced meaning. It suggests that starting from 1 and undergoing a rotation of ![equation](https://latex.codecogs.com/gif.latex?\pi) leads to -1. This equation emphasizes the essence of the RNS, highlighting the significance of rotations and unit circle positions.

In the context of the Fourier Transform, the term ![equation4](https://latex.codecogs.com/gif.latex?e^{-i\pi\omega t}) is interpreted not merely as a complex sinusoid. Instead, it embodies a series of rotations and negations along a helix, providing an alternative perspective on frequency components and signal processing.

## Euler's Formula and Helical Interpretation:

Traditionally, Euler's formula is given as:
![equation](https://latex.codecogs.com/gif.latex?e^{ix}&space;=&space;cos(x)&space;&plus;&space;isin(x))

Exponentiating with a complex number introduces trigonometric functions. 

### Imaginary Unit, ![equation](https://latex.codecogs.com/gif.latex?i):
Defined by:
![equation](https://latex.codecogs.com/gif.latex?i^2&space;=&space;-1)

In the RNS, multiplication by ![equation](https://latex.codecogs.com/gif.latex?i) signifies a quarter-turn or 90° rotation in the complex plane and a move upward along the helical axis. This idea is rooted in:
![equation](https://latex.codecogs.com/gif.latex?e^{i(\pi/2)}&space;=&space;i)

Euler's number ![equation](https://latex.codecogs.com/gif.latex?e) embodies continuous transformation. Coupled with the ![equation](https://latex.codecogs.com/gif.latex?i\pi) rotation, it results in cyclical behaviors:
![equation](https://latex.codecogs.com/gif.latex?e^{i\pi}&space;=&space;-1)

### Complex Plane Dynamics:
Multiplication by a complex number usually entails rotation and dilation. In the RNS, with ![equation](https://latex.codecogs.com/gif.latex?\pi&space;=&space;-1), multiplication primarily represents rotation, with ![equation](https://latex.codecogs.com/gif.latex?\pi) as a pivotal element.

### Algebraic-Geometric Interplay:
In the RNS, multiplication is a geometric action. For any real ![equation](https://latex.codecogs.com/gif.latex?x):
![equation](https://latex.codecogs.com/gif.latex?x&space;\times&space;\pi&space;=&space;-x)

This means that multiplying by ![equation](https://latex.codecogs.com/gif.latex?\pi) negates ![equation](https://latex.codecogs.com/gif.latex?x) algebraically and rotates it by ![equation](https://latex.codecogs.com/gif.latex?\pi) radians on the unit circle.

### RNS-Based Trigonometry:
In the RNS, trigonometric identities transform with ![equation](https://latex.codecogs.com/gif.latex?\pi) representing -1:
![equation](https://latex.codecogs.com/gif.latex?sin(\pi&space;&plus;&space;\theta)&space;=&space;-sin(\theta))
![equation](https://latex.codecogs.com/gif.latex?cos(\pi&space;&plus;&space;\theta)&space;=&space;-cos(\theta))

In the Fourier series, each term is expressed as a complex number via Euler's formula:
![equation](https://latex.codecogs.com/gif.latex?e^{i\theta}&space;=&space;cos(\theta)&space;&plus;&space;isin(\theta))

Hence, Fourier series terms are:
![equation](https://latex.codecogs.com/gif.latex?f(t)&space;=&space;a_0&space;&plus;&space;\sum_{n=1}^{\infty}&space;r_n&space;e^{i(2\pi&space;nf&space;t&space;&plus;&space;\phi_n)})

Where ![equation](https://latex.codecogs.com/gif.latex?r_n&space;=&space;\sqrt{a_n^2&space;&plus;&space;b_n^2}) is the magnitude and ![equation](https://latex.codecogs.com/gif.latex?\phi_n&space;=&space;arctan(\frac{b_n}{a_n})) is the phase.

### Waveform Compression

The ENT's helical interpretation bridges wave properties via the Fourier series. Given a wave function ![equation](https://latex.codecogs.com/gif.latex?f(t)), its Fourier series is:
![equation](https://latex.codecogs.com/gif.latex?f(t)&space;=&space;a_0&space;&plus;&space;\sum_{n=1}^{\infty}&space;\left[&space;a_n&space;cos(2\pi&space;n&space;f&space;t)&space;&plus;&space;b_n&space;sin(2\pi&space;n&space;f&space;t)&space;\right])

In the ENT, series terms correspond to numbers in rotational representation, enabling intuitive understanding of wave transformations.

This concept's extension might allow encoding intricate data, like music, as integer sets. 
![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/8e9b6e96-5dad-43d8-bc64-89640e0c4b8b)


