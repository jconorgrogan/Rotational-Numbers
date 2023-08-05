import numpy as np
import matplotlib.pyplot as plt

def number_properties_harmonic(number):
    """Determine amplitude and phase based on a number with harmonic relationships."""
    
    # Prime factors (with repetition) extraction
    prime_factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            prime_factors.append(i)
    if number > 1:
        prime_factors.append(number)
    
    # Amplitude is the number of prime factors (with repetition)
    amplitude = len(prime_factors)
    
    # Phase based on modulo 2pi
    phase = number % (2 * np.pi)
    
    return amplitude, phase, prime_factors

def number_to_waveform_prime_influence(number, rotation, amplitude, prime_factors, t):
    """Translate a number into a waveform influenced by its largest prime factor."""
    
    # Base waveform for the largest prime factor
    largest_prime = max(prime_factors)
    waveform = amplitude * np.sin(2 * np.pi * largest_prime * t + rotation)
    
    return waveform

def plot_waveform_prime_influence(number, t):
    """Generate and plot a waveform corresponding to a number influenced by its largest prime factor."""
    
    amplitude, rotation, prime_factors = number_properties_harmonic(number)
    
    # Generate the corresponding waveform
    waveform = number_to_waveform_prime_influence(number, rotation, amplitude, prime_factors, t)

    # Plot the waveform
    plt.figure(figsize=(6, 4))
    plt.plot(t, waveform)
    plt.title('Waveform for Number = {}, Rotation = {:.2f}, Amplitude = {}, Prime Factors = {}'.format(number, rotation, amplitude, prime_factors))
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)

# Define a time array
t = np.linspace(0, 1, 500)

# Test with various numbers
numbers_to_test = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers_to_test:
    plot_waveform_prime_influence(number, t)
plt.tight_layout()
plt.show()
