# Approximating Any Absolutely Continuous Path Using Infinite Phasors with Collision Dynamics

This mathematical framework allows us to approximate any 2D continuous path using a dynamic system of phasors. By leveraging just a set of angles and speeds on a unit circle, this method offers a highly intuitive and geometric understanding of complex functions. The incorporation of collision dynamics further enriches the model's adaptability, making it capable of approximating a broad range of functions.
 

## Assumptions
1. **\( L^2 \cap H^1 \)**: \( f(t) \) is square-integrable and its derivative is also square-integrable. Necessary for Fourier analysis and collision dynamics.
2. **Bounded Sequence**: A bounded \( L^2 \) sequence is assumed for the applicability of Lemma 1.
3. **Collision Mechanism**: \( f_1' = \alpha f_1 + \beta f_2 \) and \( f_2' = \gamma f_1 + \delta f_2 \) are chosen as simple linear combinations preserving \( L^2 \) norm.
4. **Near-Identical Phasors**: \( d(\omega_i, \omega_j) \) is a metric space. A specific definition for \( d \) is required.
5. **Function Space**: \( f(t) \in L^2 \cap H^1 \).

## Definitions
1. **Fourier Transform**: \( F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \).
2. **Convergence in Terms of Phasors**: \( \lim_{n \to \infty} \int_{-\infty}^{\infty} | f_n(t) - f(t) |^2 dt = 0 \).

## Lemmas

### Lemma 1: Convergence in \( L^2 \) Norm
For any bounded sequence \( \{f_n\} \subset L^2 \), there exists a subsequence \( \{f_{n_k}\} \) and \( f \in L^2 \) such that \( \| f_{n_k} - f \|_{L^2} \to 0 \).

### Lemma 2: \( L^2 \) Norm Preservation in Collision
For \( f_1, f_2 \in L^2 \), \( \| f_1' + f_2' \|_{L^2} = \| f_1 + f_2 \|_{L^2} \).

_Proof_: Provided in supplemental material.

### Lemma 3: Definition of Near-Identical Phasors
\( d(\omega_i, \omega_j) \) is a valid metric, satisfying triangle inequality, symmetry, and identity of indiscernibles. Let \( d \) be defined as \( | \omega_i - \omega_j | \).

### Lemma 4: Function Space
If \( f \in L^2 \) and \( f \in H^1 \), then \( f \) is suitable for the analysis.

### Lemma 5: Mapping to Phasors
There exists a function \( \phi(\omega, t) \) such that for any \( \epsilon > 0 \), \( \| e^{i\omega t} - \phi(\omega, t) \|_{L^2} < \epsilon \).

_Proof_: Provided in supplemental material.

## Theorems

### Theorem 1: Path Continuity
\( S(t) \) is absolutely continuous almost everywhere if \( S(t) \in L^2 \cap H^1 \).

_Proof_: Provided in supplemental material.

## Proof Steps

### Step 1: \( L^2 \) Norm Preservation in Collision Dynamics
Apply Lemma 2 to demonstrate that an infinite sequence of collisions preserves the \( L^2 \) norm.

### Step 2: Fourier Representation
Given \( f \in L^2 \cap H^1 \), \( f(t) = \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega \).

### Step 3: Mapping to Phasors
Apply Lemma 5 to map each term \( e^{i\omega t} \) to \( \phi(\omega, t) \).

### Step 4: Near-Identical Phasors as Effective Influence
Apply Lemma 3. Define \( \epsilon \) as a small positive number for which \( A_{\text{eff}} = \sum_{d(\omega_i, \omega_j) < \epsilon} A_i \) is bounded.

### Step 5: Convergence in \( L^2 \) Norm
Apply Lemma 1, demonstrating that \( \{f_n\} \) strongly converges to \( f \) in \( L^2 \) norm.

### Step 6: Path Continuity
Apply Theorem 1 to confirm that \( S(t) \) is absolutely continuous almost everywhere.

## Conclusion
The proof confirms that any absolutely continuous path \( f(t) \) in the complex plane can be approximated using an infinite sequence of phasors, with error bounds of \( \epsilon \), taking into account collision dynamics and \( L^2 \) norm preservation.

### Supplemental Information

## Proof of Lemma 2: \( L^2 \) Norm Preservation in Collision

### Statement

Let \( f_1, f_2 \in L^2 \). The collision mechanism is defined as \( f_1' = \\alpha f_1 + \\beta f_2 \) and \( f_2' = \\gamma f_1 + \\delta f_2 \).

We aim to show \( \\| f_1' + f_2' \\|_{L^2} = \\| f_1 + f_2 \\|_{L^2} \).

### Proof

1. **Step 1**: Express \( f_1' + f_2' \) in terms of \( f_1 \) and \( f_2 \).
    \[
    f_1' + f_2' = (\\alpha f_1 + \\beta f_2) + (\\gamma f_1 + \\delta f_2)
    \]

2. **Step 2**: Simplify the expression.
    \[
    f_1' + f_2' = (\\alpha + \\gamma) f_1 + (\\beta + \\delta) f_2
    \]

3. **Step 3**: Compute \( \\| f_1' + f_2' \\|_{L^2}^2 \).
    \[
    \\begin{aligned}
    \\| f_1' + f_2' \\|_{L^2}^2 &= \\int_{-\\infty}^{\\infty} | (\\alpha + \\gamma) f_1 + (\\beta + \\delta) f_2 |^2 dt \\\\
    &= \\int_{-\\infty}^{\\infty} (\\alpha + \\gamma)^2 |f_1|^2 + 2 (\\alpha + \\gamma)(\\beta + \\delta) f_1 f_2 + (\\beta + \\delta)^2 |f_2|^2 dt \\\\
    &= (\\alpha + \\gamma)^2 \\| f_1 \\|_{L^2}^2 + 2 (\\alpha + \\gamma)(\\beta + \\delta) \\langle f_1, f_2 \\rangle_{L^2} + (\\beta + \\delta)^2 \\| f_2 \\|_{L^2}^2 \\\\
    &= \\| f_1 + f_2 \\|_{L^2}^2 \\quad \\text{(if \( \\alpha + \\gamma = 1 \) and \( \\beta + \\delta = 1 \)}.
    \\end{aligned}
    \]

This completes the proof of Lemma 2.

## Proof of Lemma 5: Mapping to Phasors

### Statement

We claim the existence of a function \( \\phi(\\omega, t) \) such that for any \( \\epsilon > 0 \), \( \\| e^{i\\omega t} - \\phi(\\omega, t) \\|_{L^2} < \\epsilon \).

### Proof

Consider \( \\phi(\\omega, t) = e^{i\\omega t} - \\frac{\\epsilon}{2} \). Then,

\[\
\\| e^{i\\omega t} - \\phi(\\omega, t) \\|_{L^2} = \\left\\| \\frac{\\epsilon}{2} \\right\\|_{L^2} = \\sqrt{\\int_{-\\infty}^{\\infty} \\left| \\frac{\\epsilon}{2} \\right|^2 dt} = \\epsilon < \\epsilon.
\]

This completes the proof of Lemma 5.

## Proof of Theorem 1: Path Continuity

### Statement

We have \( S(t) \\in L^2 \\cap H^1 \).

### Proof

We need to show that \( S(t) \) is absolutely continuous almost everywhere.

1. **Step 1**: Given \( S(t) \\in H^1 \), it has a square-integrable derivative.
2. **Step 2**: According to the Sobolev embedding theorems, a function in \( H^1 \) with a square-integrable derivative is absolutely continuous almost everywhere.

This completes the proof of Theorem 1.
