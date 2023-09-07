## Theorem

Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin. Divide the circle into \( 2R \) equal slices. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

### Proof

To find the \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis, we have:

\[
y = R \sin\left(\frac{\pi}{R}\right)
\]

Substitute \( R = 2^n \):

\[
y = 2^n \sin\left(\frac{\pi}{2^n}\right)
\]

We want to find \( \lim_{{n \to \infty}} 2^n \sin\left(\frac{\pi}{2^n}\right) \).

Utilizing the limit identity \( \lim_{{x \to 0}} \frac{\sin(x)}{x} = 1 \), we rewrite the expression as:

\[
\lim_{{n \to \infty}} \left(2^n \frac{\pi}{2^n}\right) \left(\frac{\sin\left(\frac{\pi}{2^n}\right)}{\frac{\pi}{2^n}}\right)
\]

We used this identity because the expression \( \frac{\sin\left(\frac{\pi}{2^n}\right)}{\frac{\pi}{2^n}} \) approaches 1 as \( \frac{\pi}{2^n} \rightarrow 0 \), which happens as \( n \rightarrow \infty \).

The first term \( 2^n \frac{\pi}{2^n} \) simplifies to \( \pi \).

Thus, the limit becomes \( \pi \times 1 = \pi \), proving that the \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

By invoking the Squeeze Theorem indirectly through the use of the limit identity \( \lim_{{x \to 0}} \frac{\sin(x)}{x} = 1 \), we make the proof rigorous.

This concludes the proof that each of these horizontal lines approaches a multiple of \( \pi \) as \( R \) goes to infinity.


Each of these horizontal lines approaches a multiple of pi as R goes to infinity
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/2a204d04-0238-44ed-a5f4-a91fe5c68617)

