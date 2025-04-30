import math

# Function to check if a number is a perfect square
def is_perfect_square(x):
    return int(math.sqrt(x)) ** 2 == x

# Function to check if N is a Fibonacci number
def is_fibonacci(n):
    # Check if 5 * n^2 + 4 or 5 * n^2 - 4 is a perfect square
    return is_perfect_square((5 * n * n) + 4) or is_perfect_square((5 * n * n) - 4)

T = int(input("Enter number of test cases : "))
    
    # Process each test case
for _ in range(T):
    N = int(input("Enter the number : "))
    if is_fibonacci(N):
       print("IsFibo")
    else:
        print("IsNotFibo")

