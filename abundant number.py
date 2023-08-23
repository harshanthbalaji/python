sum = 0
num = int(input("Enter the number: "))
for i in range(1,num,1):
    if num%i ==0:
        print(i, end=", ")
        sum = sum + i
if sum>num:
    print(str(num)+" is an abundant number.")
else:
    print(str(num)+"is not an abundant number.")
