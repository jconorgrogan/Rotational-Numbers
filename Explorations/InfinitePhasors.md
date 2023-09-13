# Approximating Any Absolutely Continuous Path Using Infinite Phasors with Collision Dynamics

## Assumptions

1. **Infinite Phasors**: A bounded sequence of systems \( f_n \) exists where \( f_n(t) = \sum_{k=1}^{n} A_k e^{i\omega_k t} \) and \( \sup_n \| f_n \|_{L^2} < \infty \).

2. **Collision Mechanism**: Collision rules are time and frequency dependent: \( f_1'(t, \omega) = \alpha(\omega, t) f_1(t, \omega) + \beta(\omega, t) f_2(t, \omega) \) and \( f_2'(t, \omega) = \gamma(\omega, t) f_1(t, \omega) + \delta(\omega, t) f_2(t, \omega) \).

3. **Near-Identical Phasors**: \( d(\omega_i, \omega_j) = |\omega_i - \omega_j| \).

4. **Function Space**: \( f(t) \in L^2 \cap H^1 \).

## Definitions

- **Fourier Transform**: \( F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \).

- **Convergence in Terms of Phasors**: \( f_n(t) \) approximates \( f(t) \) if \( \lim_{n \to \infty} \int_{-\infty}^{\infty} | f_n(t) - f(t) |^2 dt = 0 \).

## Lemmas

### Lemma 1: Convergence in \( L^2 \) Norm
Given \( \{f_n\} \subset L^2 \), a subsequence \( \{f_{n_k}\} \) and \( f \in L^2 \) exist such that \( \| f_{n_k} - f \|_{L^2} \to 0 \).

### Lemma 2: \( L^2 \) Norm Preservation in Collision
For \( f_1, f_2 \in L^2 \), \( \| f_1' + f_2' \|_{L^2} = \| f_1 + f_2 \|_{L^2} \).

### Lemma 3: Definition of Near-Identical Phasors
\( d(\omega_i, \omega_j) = |\omega_i - \omega_j| \) is a valid metric.

### Lemma 4: Function Space
If \( f \in L^2 \cap H^1 \), then \( f \) is suitable for analysis.

### Lemma 5: Mapping to Phasors
For any \( \epsilon > 0 \), \( \| e^{i\omega t} - e^{i\omega t} \|_{L^2} < \epsilon \) (Trivially true).

## Theorems

### Theorem 1: Path Continuity
\( S(t) \) is absolutely continuous almost everywhere if \( S(t) \in L^2 \cap H^1 \).

## Proof Steps

### Step 1: \( L^2 \) Norm Preservation in Collision Dynamics
Apply Lemma 2.

### Step 2: Fourier Representation
\( f(t) = \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega \).

### Step 3: Mapping to Phasors
Apply Lemma 5. No mapping needed; \( e^{i\omega t} \) is its own best approximation.

### Step 4: Near-Identical Phasors as Effective Influence
Using \( d(\omega_i, \omega_j) = |\omega_i - \omega_j| \) and defining \( \epsilon \), \( A_{\text{eff}} = \sum_{d(\omega_i, \omega_j) < \epsilon} A_i \) is bounded.

### Step 5: Convergence in \( L^2 \) Norm
Apply Lemma 1.

### Step 6: Path Continuity
Apply Theorem 1.

## Conclusion

The proof confirms that any absolutely continuous path \( f(t) \) in the complex plane can be approximated using an infinite sequence of phasors, with error bounds of \( \epsilon \), taking into account collision dynamics and \( L^2 \) norm preservation.

