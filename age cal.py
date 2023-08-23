import datetime
def calage(year,month,day):
today=datetime.date.today()
dob=datetime.date(year,month,day)
age=int((today-dob).days/365
return age
userdob=input("enter your dob in this format'year-month-day':")
dob=user dob.split('-')
year,month,day=int(dob[0]),int(dob[1]),int(dob[2])
your age=cal age(year,month,day)
print(f"you are{your age}years old")
        
