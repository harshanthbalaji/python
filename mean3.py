sum = int(0)
num = int(input("Enter the number of values: "))
r = range(1,num+1,1)
for i in r:
    x = int(input("Enter the value "))
    sum = sum + x
mean = sum/num
print("The mean of given values is :",mean)
