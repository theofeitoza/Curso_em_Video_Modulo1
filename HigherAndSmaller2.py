num1=float(input('Type the first number:'))
num2=float(input('Type the second number:'))
num3=float(input('Type the third number:'))
smaller=num1
if(num2<num1 and num2<num3):smaller=num2
if(num3<num1 and num3<num2):smaller=num3
higher=num1
if(num2>num1 and num2>num3):higher=num2
if(num3>num1 and num3>num2):higher=num3
print(f'The higher number is:{higher}'.format(higher))
print(f'The smaller number is:{smaller}'.format(smaller))