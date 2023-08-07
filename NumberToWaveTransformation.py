import numpy as np
import matplotlib.pyplot as plt

def decompose_complex_number(number):
    """Decompose a complex number into its real part, imaginary part, and phase."""
    if not isinstance(number, complex):
        raise ValueError("Input should be a complex number.")
    
    real_part = number.real
    imaginary_part = number.imag
    phase = np.angle(number)
    
    return real_part, imaginary_part, phase

def number_to_waveform_complex(number, t, base_frequency=1):
    """Translate a complex number into a waveform."""
    real_part, imaginary_part, phase = decompose_complex_number(number)
    waveform = real_part * np.cos(base_frequency * 2 * np.pi * t + phase) + \
               imaginary_part * np.sin(base_frequency * 2 * np.pi * t + phase)
    return waveform

def plot_waveform_complex(number, t):
    """Generate and plot a waveform corresponding to a complex number."""
    real_part, imaginary_part, phase = decompose_complex_number(number)
    waveform = number_to_waveform_complex(number, t)

    plt.figure(figsize=(6, 4))
    plt.plot(t, waveform, label=f"Real={real_part}, Imaginary={imaginary_part}")
    plt.title(f'Waveform for Number {number}, Phase = {phase:.2f}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

# Define a time array
t = np.linspace(0, 1, 500)

# Test with complex numbers
numbers_to_test = [5+3j, 7+1j]
for number in numbers_to_test:
    plot_waveform_complex(number, t)

plt.tight_layout()
plt.show()
