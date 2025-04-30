def count_divisible_positions(n):
    count = 0
    str_n = str(n)
    
    for digit in str_n:
        if digit != '0' and n % int(digit) == 0:  # Ensure digit is not zero and divides N
            count += 1
            
    return count

# Read number of test cases
T = int(input("Enter number of test cases : "))

# Process each test case
for _ in range(T):
    N = int(input())
    print(count_divisible_positions(N))
