def maximizing_xor(L, R):
    max_xor = 0  # Initialize the maximum XOR value

    # Loop over all pairs A and B where L <= A <= B <= R
    for A in range(L, R + 1):
        for B in range(A, R + 1):  # Start from A to avoid repeated pairs
            max_xor = max(max_xor, A ^ B)  # Update max_xor if we get a larger XOR

    return max_xor

L = int(input("Enter L : "))
R = int(input("Enter R : "))


print(maximizing_xor(L, R))