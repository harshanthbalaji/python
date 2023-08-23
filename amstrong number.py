n=int(input("enter the value of n"))
s=0
n1=n
while n!=0:
    d=n%10
    s=s+d*d*d
    n=n//10
if s==n1:
    print("n is amstrong number")
else:
    print("n is not an amstrong number")
