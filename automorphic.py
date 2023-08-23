n=int(input("enter the value of n"))
square=n*n
f=0
while n!=0:
    squarer=square%10
    number=n%10
    if squarer!=number:
        f=7
        break
    else:
        square=square//10
        n=n//10
if f==0:
    print("it is  an automorphic number")
else:
    print("it is not a automorphic number")
    
       
    
    
    
    


