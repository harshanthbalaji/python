n=int(input("enter the value of n"))
s=0
n1=n
while n!=0:
    d=n%10
    s=s*10+d
    n=n//10
if s==n1:
    print("n is pallindrome")
else:
    print("n is not an pallindrome number")
print("reverse",s)    
