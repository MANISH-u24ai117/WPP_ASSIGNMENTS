import random

# Generate 100 random integers (either 0 or 1)
random_integers = [random.choice([0, 1]) for _ in range(100)]

# Initialize variables to track the longest run of zeros
longest_run = 0
current_run = 0

# Loop through the list to find the longest run of zeros
for num in random_integers:
    if num == 0:
        current_run += 1
        longest_run = max(longest_run, current_run)
    else:
        current_run = 0

# Output the results
print(f"Random list: {random_integers}")
print(f"The longest run of zeros is: {longest_run}")
