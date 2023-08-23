name=input("enter name")
p=int(input("enter the price"))
if p<=10000:
    discountp=5/100*p
elif p<=15000:
    discountp=10/100*p
elif p<=20000:
    discountp=15/100*p
else:
    discountp=20/100*p
net=p-discountp
print("enter name",name,"discount is",discountp,"net is",net)
