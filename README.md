
## 1. Introduction

Rotational Number Theory (RNT) is an attempt to find a novel way to visualize mathmatics (And a real way to find prime factors!)  

In RNT, each natural number `n` is depicted by `n` equidistant nodes on a unit circle.

![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/d94798c6-aa7c-4ece-84b2-6a17fab5192b)

The position of a node representing the `k`-th number is determined by the angle:

![equation](https://latex.codecogs.com/gif.latex?\theta_k&space;=&space;\frac{2\pi(k-1)}{n})

## 2. Prime and Factor Identification via Rotational Overlap

This geometric representation leads to an intuitive method for discerning prime numbers and factorizing composites.

If you rotate each set of nodes by their respective angles, no two nodes will overlap with the starting positions of any nodes throughout a full rotation unless a divisor relationship exists between them.

Here is a visual representation: 7 (red dots, equally spaced) is a factor of 21

![circle_overlap](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/320e879d-428f-42bb-a3cb-79ba8d6a1311)

2 does not "fit" within the 5 when you rotate is. Same with 3 and 4.  5 is therefore prime

![circle_overlap2](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/ebc9b49f-44c9-4adc-bad1-b6bcdf038c3f)

## 3. Patterns

Displaying these numbers in linearly expanding concentric circles is an interesting way of seeing number patterns.

Here are the first 500 numbers (2-500)
<img width="848" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/8b873bd5-5907-49ec-972b-9bdb1355d6e4">

100 primes v 100 composites
<img width="1152" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/4f3cd8fe-e182-46a0-890e-a0f18f5551c5">

Here I scaled composites to match the density of the primes. It appears that the density and scaling itself explains much/most of the interesting shapes and pattern differences
<img width="1406" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/464f30da-eb4c-4428-afb7-79f43bd23520">

Here is a zoomed-in plot of all composites, linearly scaling for each subsequent composite number
<img width="688" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/a35158a7-e5df-4aa7-839e-17badd89bda3">

And here is a plot of all prime numbers up to 50, linearly scaling for each prime addition. Each color is a different type of prime<img width="688" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/9a31711f-52bb-474e-b352-cce2ac3c2cee">

16 primary angles that show up, with these 4 the most obvious, especially at lower n
<img width="695" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/fe27d0ac-ba97-4243-bcad-f0667483afd8">


## 3. Operations in RNT

![image](https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/29b221f0-c7b1-48f9-bdf8-db6c8175d570)

RNT offers a geometric perspective on the relationships between numbers and mathematical operations, Addition involves appending new nodes and recalibrating to maintain equidistance. It’s a disruption of the existing structure, whereas multiplication and division, being scaling operations, maintain a certain symmetry and uniformity. You will notice a fair amount of connections to signal processing:

| Operator         | Mathematical Basis          | Effect on Nodes                                    | Core Mathematical Components          | DSP Connection                 |
|------------------|-----------------------------|----------------------------------------------------|--------------------------------------|--------------------------------|
| Addition         | Addition of nodes           | Addition of new nodes; each recalibrated to maintain equidistance | \(\theta(n) = \frac{2\pi(n-1)}{n+a}\)  | Superposition Principle        |
| Subtraction      | Removal of nodes            | Removal of nodes; each recalibrated to maintain equidistance  | \(\theta(n) = \frac{2\pi(n-1)}{n-a}\)  | Wave Cancellation (Destructive Interference) |
| Multiplication   | Replication and redistribution of nodes | Repetition of nodes based on multiplication factor; each copy rotated by an angle relative to previous | \(\theta(n, k) = \frac{2\pi(n-1)}{a} + \frac{2\pi(k-1)}{b}\)  | Frequency Modulation          |
| Division         | Counter-rotation and scaling | Redistribution of nodes based on division factor; each copy rotated by an angle relative to previous | \(\theta(n, k) = \frac{2\pi(n-1)}{a} - \frac{2\pi(k-1)}{b}\) | Frequency Demodulation        |
| Fraction (Decimal) | Partial completion of circle | Placement of nodes less than a full circle               | \(\theta(n) = \frac{2\pi(n-1)}{n+\alpha}\) (where \(\alpha < 1\)) | Phase Modulation              |
| Negation         | Inversion of nodes          | Nodes flipped across the origin                          | \(\theta(n) = -\frac{2\pi(n-1)}{n}\) | Wave Inversion (180 Degree Phase Shift) |
| Absolute value   | Positioning nodes in positive half | All nodes moved to the positive half                      | \(\theta(n) = \left|\frac{2\pi(n-1)}{n}\right|\) | Rectification (All Positive Wave) |
| Exponentiation   | Formation of expanding spiral | Nodes placed in expanding spiral pattern                  | \(\theta(n) = r^{(n-1)}e^{\frac{2\pi i(n-1)}{n}}\) | Amplitude Modulation          |
| Logarithm        | Formation of contracting spiral | Nodes placed in contracting spiral pattern                | \(\theta(n) = \log(r^{(n-1)})e^{\frac{2\pi i(n-1)}{n}}\) | Signal Compression             |
| Modulo           | Folding back of nodes       | Nodes beyond modulo number are folded back                | \(\theta(n) = \frac{2\pi((n-1) \mod m)}{m}\) | Wave Wrapping (Overflow Handling) |

 
**The Complex Plane**

In the RNS, multiplication in the complex domain is visualized as a combination of rotation in the complex plane and movement along a helix. This helical interpretation offers a three-dimensional depth to the traditional two-dimensional complex plane, enhancing our understanding of operations involving imaginary components.

When a complex number is multiplied by a factor of the form ![equation](https://latex.codecogs.com/gif.latex?e^{i\theta}), it corresponds to a rotation of that number by an angle \(\theta\) in the complex plane. Thus, multiplying by ![equation](https://latex.codecogs.com/gif.latex?2i=e^{i(2\pi)}) represents a quarter-turn or 90° rotation, and due to the imaginary component, it also results in an upward movement along the helix's axis.

<img width="372" alt="image" src="https://github.com/jconorgrogan/Grogan-Rotational-Number-Theory/assets/130090573/4a531cc2-bc2d-4152-b608-fc4f2cc16a11">


The term ![equation](https://latex.codecogs.com/gif.latex?\pi) represents a 180° operation or half-rotation. Multiplying by ![equation](https://latex.codecogs.com/gif.latex?\pi) reflects the number to its opposite point on the unit circle.

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

This concept's extension might allow encoding of intricate data, like music, as integer sets. 


