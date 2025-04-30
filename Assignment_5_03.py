T = int(input("Enter number of test cases : "))

while(T):
   
    T-=1
    s=input("Enter String : ")
    s=list(s)
    size=len(s)
    ch=False # create a flag
    
    if(s[0] * size == s): # if the string has all same characters
        print("No Answer")
    else:
        for i in range(size-2, -1, -1): # starts from last second element to find pivot 
           
            for j in range(size-1, i, -1): # to find ch which is greater than it on the right
                
                if(s[i]<s[j]):
                   
                    s[i], s[j] = s[j], s[i]
                    s= s[:i+1] + s[size-1 : i :-1]
                    ch=True # break the loop when flag becomes true
                   
                    break
            if ch:
                break
        print(''.join(s)) # turn list back to string and then print it