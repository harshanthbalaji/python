a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a+b>c and b+c>a and c+a>b:
    print("triangle is possible")
    if a==b and b==c and c==a:
        print("equilateral triangle")
    elif a==b or b==c or c==a:
        print("isoceles triangle")
    else:
        print("scalene triangle")
else:
     print("triangle is not possible")
