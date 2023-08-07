import numpy as np
import matplotlib.pyplot as plt

def number_properties_harmonic(number):
    """Determine amplitude and phase based on a number with harmonic relationships."""
    
    # Decompose the number into its integer and fractional parts
    integer_part = int(number)
    fractional_part = number - integer_part
    
    # Prime factors (with repetition) extraction
    prime_factors = []
    i = 2
    while i * i <= integer_part:
        if integer_part % i:
            i += 1
        else:
            integer_part //= i
            prime_factors.append(i)
    if integer_part > 1:
        prime_factors.append(integer_part)
    
    # Amplitude is the product of prime factors
    amplitude = np.prod(prime_factors)
    
    # Phase based on modulo 2pi, with an adjustment based on the fractional part
    phase = (number % 1) * (2 * np.pi)
    
    # Polarization
    polarization = (-1)**(integer_part % 2)
    
    return amplitude, phase, polarization, prime_factors

def number_to_waveform_prime_influence(number, rotation, amplitude, polarization, prime_factors, t):
    """Translate a number into a waveform influenced by its prime factors."""

    # Start with a base waveform of zeros
    waveform = np.zeros_like(t)

    # Each prime factor contributes a wave
    for prime in prime_factors:
        wave = (amplitude / prime) * np.sin(2 * np.pi * prime * t + rotation)

        # Add the wave to the current waveform (without damping)
        waveform += wave

    # Apply polarization
    waveform *= polarization

    return waveform


def plot_waveform_prime_influence(number, t):
    """Generate and plot a waveform corresponding to a number influenced by its prime factors."""

    number = float(number)  # Convert to float
    amplitude, rotation, polarization, prime_factors = number_properties_harmonic(number)
    
    waveform = number_to_waveform_prime_influence(number, rotation, amplitude, polarization, prime_factors, t)


    plt.figure(figsize=(6, 4))
    plt.plot(t, waveform)
    plt.title('Waveform for Number = {}, Rotation = {:.2f}, Amplitude = {}, Polarization = {}, Prime Factors = {}'.format(number, rotation, amplitude, polarization, prime_factors))
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)

# Define a time array
t = np.linspace(0, 1, 500)

# Test with various numbers
numbers_to_test = [5,7]
for number in numbers_to_test:
    plot_waveform_prime_influence(number, t)

plt.tight_layout()
plt.show()
