n=int(input("enter n"))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")
if n%3==0 and n%5==0:
  print(n,"is divisible by both 3 and 5")
elif n%3==0 and n%5!=0: 
  print(n,"is divisible by 3 but not by 5")
elif n%3!=0 and n%5==0:
  print( n,"is not divisible by 3 and divisible by 5")
else:
    print(n,"is not divisible by both 3 and 5")
