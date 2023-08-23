n=int(input("enter n"))
c=0
for i in range(2,n//2+1,1):
    if(n%i==0):
        c=c+1
        print(i)
if c==0:
    print(n,"is prime")
else:
    print(n,"is composite")
        
