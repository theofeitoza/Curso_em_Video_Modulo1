print('I\'m a travel calculator')
d1=int(input('Enter the distance of your trip: '))
if(d1<=200):
    v1=d1*0.5
    print('The cost of your trip will be ${:.2f}'.format(v1))
else:
    v2=d1*0.45
    print('The cost of your trip will be ${:.2f}'.format(v2))