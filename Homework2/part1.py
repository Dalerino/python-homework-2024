# Convert # of years to days, weeks, months, hours
Years = int(input("Enter number of years: "))
Days=365
Weeks=52
Months=12
Hours=24*365
print()

def days():
    return Years*Days
print(f"Number of days in {Years} years:",days())

def weeks():
    return Years*Weeks
print(f"Number of weeks in {Years} years:",weeks())

def months():
    return Years*Months
print(f"Number of months in {Years} years:",months())

def hours():
    return Years*Hours
print(f"Number of hours in {Years} years:",hours())

