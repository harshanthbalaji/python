sum = 0
product =1
number = int(input("Enter the number to test if it is a spy number or not:"))
a  = str(number)
for i in a:
    sum = sum + int(i)
    product = product * int(i)
if sum == product:
    print("Yes da! It is a Spy number...  What now?")
else:
    print("Poda dei... Spy number lethu da!")
