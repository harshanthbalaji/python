n = int(input("Enter the \"n\" value: "))
S = 0
sign = True
for i in range(2,n+1,2):
    if sign:
        S = S+i
        sign = False
    else:
        S = S-i
        sign = True
print("S = "+str(S))
