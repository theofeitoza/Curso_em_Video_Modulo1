v1=int(input('what is the car speed?'))
if(v1>80):
    multa=(v1-80)*7
    print('You exceeded the speed limit and were fined in ${:.2f}'.format(multa))
else:
    print('Congratulations, you are on the speed limit')