import numpy as np

# Sample numpy array with strings
arr = np.array(["apple", "banana", "cherry", "date", "elderberry"])

# Ensure each string is 15 characters long with '_' padding
left_justified = np.array([s.ljust(15, '_') for s in arr])
right_justified = np.array([s.rjust(15, '_') for s in arr])
centered = np.array([s.center(15, '_') for s in arr])

# Print the results
print("Left Justified:")
print(left_justified)
print("\nRight Justified:")
print(right_justified)
print("\nCentered:")
print(centered)
