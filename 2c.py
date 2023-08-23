n = int(input("Enter the \"n\" value: "))
s=0
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        s = s + j
print("The answer is :" + str(s))
