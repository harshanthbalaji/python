
a = 1
b = 1
S = a+b
n = int(input("Enter the \"n\" value: "))
for i in range(3,n+1,1):
    print(a, end="+")
    temp = a + b
    a = b
    b = temp
    S = S + a
print(" = " + str(S))
