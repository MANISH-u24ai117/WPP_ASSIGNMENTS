# Sherlock and Squares
import math

T = int(input("Enter number of test cases : "))

for _ in range(T):
    A = int(input("Enter integer A : "))
    B = int(input("Enter integer B : "))

    # Find the smallest integer whose square is >= A
    start = math.ceil(math.sqrt(A))
    # Find the largest integer whose square is <= B
    end = math.floor(math.sqrt(B))

    # The count of perfect squares is the count of integers between start and end, inclusive
    if start > end:
        print(0)
    else:
        print(end - start + 1)
