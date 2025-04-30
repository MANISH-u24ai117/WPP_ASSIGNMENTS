def max_pieces(K):
    # Balanced split of cuts
    h = K // 2
    v = K - h
    
    # The number of pieces is (h+1) * (v+1)
    return (h + 1) * (v + 1)

T = int(input("Enter number of test cases : "))

for _ in range(T):
   
    K = int(input("Enter number of cuts(K) : "))
    print(max_pieces(K))