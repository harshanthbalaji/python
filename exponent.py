x = ""
base = input("Enter the base charecter : ")
expo = int(input("Enter the exponent number : "))
expo = str(expo)
for i in range(0,len(expo),1):
    l = expo[i]
    int(l)
    match l:
        case 1:
            x = x+"¹"
        case 2:
            x = x+"²"
        case 3:
            x = x+"³"
        case 4:
            x = x+"⁴"
        case 5:
            x = x+"⁵"
        case 6:
            x = x+"⁶"
        case 7:
            x = x+"⁷"
        case 8:
            x = x+"⁸"
        case 9:
            x = x+"⁹"
        case 0:
            x = x+"⁰"
print (base+x)
