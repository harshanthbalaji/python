#program for calculating profit and loss
cp=int(input("enter cp"))
sp=int(input("enter sp"))
if sp>cp:
    print("there is a profit")
    profit=sp-cp
    profitp=profit*100/cp
    print("profit is",profit,"profit percentage is",profitp)
elif sp==cp:
    print("neither profit nor loss")
else:
    print("there is a loss")
    loss=cp-sp
    lossp=loss/cp*100
    print("loss is",loss,"loss percentage is",lossp)
          
    
