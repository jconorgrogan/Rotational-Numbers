from math import pi

def rotate_overlap_check(n, tolerance=1e-9):
    """Check if two nodes of n overlap with two nodes of any number from 2 to n-1 when rotated fully."""
    
    angles_n = [(2 * pi / n) * i for i in range(n)]
    
    for k in range(2, n):
        angles_k = [(2 * pi / k) * i for i in range(k)]
        
        # Rotate both n and k and check for two overlapping nodes at each step
        for rotation in range(n):  # Rotate n steps
            overlaps = [angle for angle in angles_n if any(abs((angle + 2*pi*rotation/n) % (2*pi) - a) < tolerance for a in angles_k)]
            
            if len(overlaps) >= 2:
                return True  # n is composite
                
    return False  # n is prime

# Determine overlap behavior for numbers up to 50
rotate_overlap_results = {n: rotate_overlap_check(n) for n in range(2, 51)}
print(rotate_overlap_results)
