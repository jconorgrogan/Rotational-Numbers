## Theorem
Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin. Divide the circle into \( 2R \) equal slices. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

## Proof
1. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis is:
   \[
   y = R \sin\left(\frac{\pi}{R}\right)
   \]

2. Substituting \( R = 2^n \):
   \[
   y = 2^n \sin\left(\frac{\pi}{2^n}\right)
   \]

3. We want to find the limit as \( n \rightarrow \infty \):
   \[
   \lim_{{n \to \infty}} 2^n \sin\left(\frac{\pi}{2^n}\right)
   \]

4. Utilizing the limit identity \( \lim_{{x \to 0}} \frac{\sin(x)}{x} = 1 \), multiply and divide by \( \frac{\pi}{2^n} \):
   \[
   \lim_{{n \to \infty}} \left(2^n \frac{\pi}{2^n}\right) \left(\frac{\sin\left(\frac{\pi}{2^n}\right)}{\frac{\pi}{2^n}}\right)
   \]

5. As \( n \rightarrow \infty \), \( \frac{\pi}{2^n} \rightarrow 0 \), making the second term approach 1. The first term is \( \pi \).

6. Therefore, the limit is \( \pi \times 1 = \pi \).

This proves that the \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

Each of these horizontal lines approaches a multiple of pi as R goes to infinity
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/2a204d04-0238-44ed-a5f4-a91fe5c68617)

