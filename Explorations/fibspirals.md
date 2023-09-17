## Fibonacci Spiral and the Golden Ratio

Let \( F_n \) denote the \( n \)-th Fibonacci number, with \( F_0 = 0 \) and \( F_1 = 1 \). Then, \( F_{n+1} = F_n + F_{n-1} \) for \( n \geq 1 \).

![Equation 1](https://latex.codecogs.com/gif.latex?F_{n&plus;1}&space;=&space;F_n&space;&plus;&space;F_{n-1})

Consider a Fibonacci spiral constructed using quarter-circle arcs, where the radius of the \( n \)-th arc is \( F_n \).

The arc length \( L_n \) of the \( n \)-th quarter-circle is given by:

![Equation 2](https://latex.codecogs.com/gif.latex?L_n&space;=&space;\frac{\pi&space;F_n}{2})

The ratio \( R_n \) of consecutive arc lengths is:

![Equation 3](https://latex.codecogs.com/gif.latex?R_n&space;=&space;\frac{L_{n&plus;1}}{L_n}&space;=&space;\frac{F_{n&plus;1}}{F_n})

As \( n \) approaches infinity, the limit of \( R_n \) is:

![Equation 4](https://latex.codecogs.com/gif.latex?\lim_{{n&space;\to&space;\infty}}&space;R_n&space;=&space;\lim_{{n&space;\to&space;\infty}}&space;\frac{F_{n&plus;1}}{F_n}&space;=&space;\phi)

where \( \phi \approx 1.618 \) is the Golden Ratio.

Thus, in this specific geometric construction of the Fibonacci spiral, the ratio of the lengths of consecutive arcs converges to the Golden Ratio.

