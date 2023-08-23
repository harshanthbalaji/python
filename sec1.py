n=int(input("enter no of days"))
year=n//360
left=n%360
month=left//360
days=left%30
print(year,"year",month,"month",days,"days")
