from datetime import date
print('Hello, I guess if you typed a leap year')
typed_year=int(input('Type a year (Type 0 to current year):'))
if(typed_year==0):
    typed_year=date.today().year
if(typed_year%4==0 and typed_year%100!=0  or typed_year%400==0):
    print(f'{typed_year} is a leap year')
else:
    print(f'{typed_year} isn\'t a leap year')