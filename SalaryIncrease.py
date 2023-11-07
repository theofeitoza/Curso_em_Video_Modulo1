print('Find the salary increase')
salary=float(input('Type the salary:R$'))
percentage=int(input('Type the increase percentage:R$'))
if(salary<=2000):
    s2=salary+(salary*percentage/100)
else:
    print('because of the fees, the salary increased 5% more')
    s2=salary+(salary*(percentage+5)/100)
print(f'Your salary of ${salary} received an increase to ${s2}')