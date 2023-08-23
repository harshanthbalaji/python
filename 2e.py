n = int(input("Enter the \"n\" value: "))
for i in range(1,n+1,1):
    s = 0
    p = 1
    for j in range(1,i+1,1):
        s = s + j
        p = p * j
print("The answer is :" + str(s/p))
