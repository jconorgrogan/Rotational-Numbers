### Theorem:

For a circle with radius \( R \) and \( n \) equally spaced nodes, the only values of \( n \) that allow the distance \( D \) between adjacent nodes to fit an integer number of times across the circumference of the circle are \( n = 2 \) and \( n = 6 \).

### Proof:

1. **Define the distance \( D \):**
   The distance \( D \) between adjacent nodes is given by:
   \[
   D = 2R \sin\left(\frac{\pi}{n}\right)
   \]

2. **Analyze the case for \( n = 2 \):**
   For \( n = 2 \), the expression for \( D \) becomes:
   \[
   D = 2R \sin\left(\frac{\pi}{2}\right) = 2R
   \]
   Since \( D \) is equal to the diameter, it fits exactly \( \frac{1}{2} \) times across the circumference, and \( n = 2 \) is a valid case.

3. **Analyze the case for \( n = 6 \):**
   For \( n = 6 \), the expression for \( D \) becomes:
   \[
   D = 2R \sin\left(\frac{\pi}{6}\right) = R
   \]
   Since \( D \) is equal to the radius, it fits exactly once across the radius, and \( n = 6 \) is a valid case.

4. **Show that no other \( n < 6 \) satisfies the condition:**
   For \( n = 3, 4, 5 \), the values of \( D \) do not fit an integer number of times across the circumference:
   - \( n = 3 \): \( D = R\sqrt{3} \)
   - \( n = 4 \): \( D = \sqrt{2}R \)
   - \( n = 5 \): \( D = 2R \sin\left(\frac{\pi}{5}\right) \)
   None of these values fit an integer number of times across the circumference.

5. **Show that no \( n > 6 \) satisfies the condition:**
   For \( n > 6 \), the expression \( n \sin\left(\frac{\pi}{n}\right) < \pi \), leading to a contradiction. No \( n > 6 \) can satisfy the condition.
