def min_operations_to_palindrome(s):
    operations = 0
    n = len(s)
    
    # Compare characters from both ends
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))  # Add difference to operations # ord -> ASCII VALUE # abs -> convert -ve to +ve
    
    return operations

T = int(input("Enter number of test cases : "))

# Process each test case
for _ in range(T):
    s = input("Enter the string : ").strip()   # strip() -> removes whitespaces,new lines & tabs from the string
    print(min_operations_to_palindrome(s))
