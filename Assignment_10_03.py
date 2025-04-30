import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i, new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                magic_square[i, j] = n * n + 1 - magic_square[i, j]
    
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square_size = half_n * half_n
    small_magic = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)
    
    for i in range(half_n):
        for j in range(half_n):
            magic_square[i, j] = small_magic[i, j]
            magic_square[i + half_n, j + half_n] = small_magic[i, j] + 3 * sub_square_size
            magic_square[i, j + half_n] = small_magic[i, j] + 2 * sub_square_size
            magic_square[i + half_n, j] = small_magic[i, j] + sub_square_size
    
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
        for j in range(n - k, n):
            magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
    
    j_switch = k + 1
    magic_square[half_n - 1, j_switch], magic_square[half_n, j_switch] = (
        magic_square[half_n, j_switch], magic_square[half_n - 1, j_switch]
    )
    
    return magic_square

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

sizes = [4, 5, 6, 7, 8]
for size in sizes:
    print(f"Magic Square of size {size}:")
    print(generate_magic_square(size))
    print("\n")
