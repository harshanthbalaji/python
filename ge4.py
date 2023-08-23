# the try/except block
# the try will execute if there are no exceptions
try:
    # we are getting day, month, and year using input() function
    day = input('Enter day:')
    month = input('Enter month:')
    year = input('Enter year:')
    # creating a variable called age_result and we are also calling the claculate_age function
    age_result = calculate_age(int(day), int(month), int(year))
    print(f'You are {age_result} years old')
    
# the except will catch all errors
except:
    print(f'Failed to calculate age, either day or month or year is invalid')
