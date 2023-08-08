**Theorem (Euler's Rotational Theorem):**
In the Rotational Number System, the exponential function e^(iθ) is equivalent to a rotation by an angle θ in the complex plane, leading to a complex number given by:
![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%20%5Ccos%20%5Ctheta%20&plus;%20i%20%5Csin%20%5Ctheta)

**Proof:**

1. **Define the complex exponential function:**
   We begin by defining the complex exponential function using the Taylor series expansion:
   ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%201%20&plus;%20i%5Ctheta%20-%20%5Cfrac%7B%5Ctheta%5E2%7D%7B2%21%7D%20-%20%5Cfrac%7Bi%5Ctheta%5E3%7D%7B3%21%7D%20&plus;%20%5Cfrac%7B%5Ctheta%5E4%7D%7B4%21%7D%20&plus;%20%5Cldots)

2. **Separate real and imaginary parts:**
   Separate the real and imaginary parts of the expression:
   ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%20%5Cleft%281%20-%20%5Cfrac%7B%5Ctheta%5E2%7D%7B2%21%7D%20&plus;%20%5Cfrac%7B%5Ctheta%5E4%7D%7B4%21%7D%20-%20%5Cldots%5Cright%29%20&plus;%20i%5Cleft%28%5Ctheta%20-%20%5Cfrac%7B%5Ctheta%5E3%7D%7B3%21%7D%20&plus;%20%5Cfrac%7B%5Ctheta%5E5%7D%7B5%21%7D%20-%20%5Cldots%5Cright%29)

3. **Recognize the Taylor series of cosine and sine:**
   Notice that the real part is the Taylor series expansion for ![equation](https://latex.codecogs.com/gif.latex?%5Ccos%20%5Ctheta) and the imaginary part is the Taylor series expansion for ![equation](https://latex.codecogs.com/gif.latex?%5Csin%20%5Ctheta):
   ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%20%5Ccos%20%5Ctheta%20&plus;%20i%20%5Csin%20%5Ctheta)

4. **Connect to rotations in the complex plane:**
   A complex number of the form ![equation](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D) can be interpreted as a rotation by angle ![equation](https://latex.codecogs.com/gif.latex?%5Ctheta) in the complex plane. This directly corresponds to the Euler's formula in traditional mathematics.

This understanding allows us to connect linear operations (exponentiation) with nonlinear operations (rotation) and can lead to new insights in signal processing, quantum mechanics, and more.
