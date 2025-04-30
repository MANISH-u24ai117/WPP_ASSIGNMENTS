import pandas as pd

# Given series
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to upper case
s_upper = s.str.upper()
print("Upper case:\n", s_upper)

# Convert to lower case
s_lower = s.str.lower()
print("\nLower case:\n", s_lower)

# Find length of each string
s_length = s.str.len()
print("\nLength of each string:\n", s_length)
