num1=float(input('Type the first number:'))
num2=float(input('Type the second number:'))
num3=float(input('Type the third number:'))

if(num1>num2 and num1>num3):
    print(f'The higher number is:{num1}')
    if(num2>num3):
        print(f'The smaller number is:{num3}')
    else:
        print(f'The smaller number is:{num2}')

elif(num2>num1 and num2>num3):
    print(f'The higher number is:{num2}')
    if(num1>num3):
        print(f'The smaller number is:{num3}')
    else:
        print(f'The smaller number is:{num1}')
        
elif(num3>num2 and num3>num1):
    print(f'The higher number is:{num3}')
    if(num1>num2):
        print(f'The smaller number is:{num2}')
    else:
        print(f'The smaller number is:{num1}')