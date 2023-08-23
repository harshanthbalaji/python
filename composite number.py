num = int(input("Enter a number to check if it is a Composite number: "))
comp = 2
if num>1:
    comp = 0
    for i in range(2,num,1):
        if num%i == 0:
            comp = 1
if comp == 0:
    print("No. The number you entered isn't a composite number. It is a prime number.")
elif comp ==1:
    print("Yes, the number you entered is a composite number. ")
else:
    print("Please check your input. Doesn't seem right to me. You must have entered a universal number(1), or zero(0) or a negative number. \nEnter a positive number greater than 1.")
