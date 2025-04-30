def digital_root(n):
   
    # Keep summing the digits of n until we get a single digit
   
    while n >= 10:  # While n has more than one digit
   
        n = sum(int(digit) for digit in str(n))  # Sum the digits of n
   
    return n  # return the single digit 

n = int(input("Enter the number : "))
print(digital_root(n))  
