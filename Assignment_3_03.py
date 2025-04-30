def utopian_tree_growth(n):
    height = 1  # Initial height of the tree
    for cycle in range(1, n + 1):
        if cycle % 2 == 1:  # Odd cycle (monsoon) -> Double the height
            height *= 2
        else:  # Even cycle (summer) -> Increase by 1
            height += 1
    return height

T = int(input("Enter number of test cases : "))
for _ in range(T):
    N = int(input("Enter number of cycles : ")) 
    print(utopian_tree_growth(N))