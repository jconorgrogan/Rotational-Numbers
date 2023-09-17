## Fibonacci Spiral and the Golden Ratio

Let \( F_n \) denote the \( n \)-th Fibonacci number, defined as follows:

\[ F_0 = 0, \quad F_1 = 1, \quad F_{n+1} = F_n + F_{n-1} \quad \\text{for} \quad n \\geq 1 \]

![Equation 1](https://latex.codecogs.com/gif.latex?F_0%20%3D%200%2C%20%5Cquad%20F_1%20%3D%201%2C%20%5Cquad%20F_%7Bn%2B1%7D%20%3D%20F_n%20%2B%20F_%7Bn-1%7D%20%5Cquad%20%5Ctext%7Bfor%7D%20%5Cquad%20n%20%5Cgeq%201)

Consider a Fibonacci spiral constructed using quarter-circle arcs. The radius of the \( n \)-th arc is \( F_n \).

The arc length \( L_n \) of the \( n \)-th quarter-circle is given by:

\[ L_n = \\frac{\\pi F_n}{2} \]

![Equation 2](https://latex.codecogs.com/gif.latex?L_n%20%3D%20%5Cfrac%7B%5Cpi%20F_n%7D%7B2%7D)

The ratio \( R_n \) of consecutive arc lengths is:

\[ R_n = \\frac{L_{n+1}}{L_n} = \\frac{F_{n+1}}{F_n} \]

![Equation 3](https://latex.codecogs.com/gif.latex?R_n%20%3D%20%5Cfrac%7BL_%7Bn%2B1%7D%7D%7BL_n%7D%20%3D%20%5Cfrac%7BF_%7Bn%2B1%7D%7D%7BF_n%7D)

As \( n \) approaches infinity, the limit of \( R_n \) is:

\[ \\lim_{{n \\to \\infty}} R_n = \\lim_{{n \\to \\infty}} \\frac{F_{n+1}}{F_n} = \\phi \]

![Equation 4](https://latex.codecogs.com/gif.latex?%5Clim_{{n%20%5Cto%20%5Cinfty}}%20R_n%20%3D%20%5Clim_{{n%20%5Cto%20%5Cinfty}}%20%5Cfrac%7BF_%7Bn%2B1%7D%7D%7BF_n%7D%20%3D%20%5Cphi)

where \( \\phi \\approx 1.618 \) is the Golden Ratio.

Therefore, in this specific geometric construction of the Fibonacci spiral, the ratio of the lengths of consecutive arcs converges to the Golden Ratio.
