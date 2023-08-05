from math import pi

def rotation_overlap(n, tolerance=1e-9):
    """Check if two nodes of n overlap with two nodes of any number from 2 to n-1 when rotated fully. 
    Return the numbers for which this overlap occurs."""
    
    angles_n = [(2 * pi / n) * i for i in range(n)]
    overlap_numbers = []
    
    for k in range(2, n):
        angles_k = [(2 * pi / k) * i for i in range(k)]
        
        # Rotate both n and k and check for two overlapping nodes at each step
        for rotation in range(n):  # Rotate n steps
            overlaps = [angle for angle in angles_n if any(abs((angle + 2*pi*rotation/n) % (2*pi) - a) < tolerance for a in angles_k)]
            
            if len(overlaps) >= 2:
                overlap_numbers.append(k)
                break  # Once overlap is found for a number k, no need to check further rotations
                
    return overlap_numbers

# Determine overlap behavior for numbers up to 50
rotation_overlap_results = {n: rotation_overlap(n) for n in range(2, 51)}
print(rotation_overlap_results)
