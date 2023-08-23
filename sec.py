n=int(input("enter number of days"))#n=1000
year=n//360 #1000//360=2
left=n%360#1000%360 
month=left//30
days=left%30
print(year,"year",month,"month",days,"days")

