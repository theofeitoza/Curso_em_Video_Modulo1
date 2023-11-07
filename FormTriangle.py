n1=float(input('Enter the size of the first line:'))
n2=float(input('Enter the size of the second line:'))
n3=float(input('Enter the size of the third line:'))
if(n1+n2>n3 and n1+n3>n2 and n2+n3>n1):
    print('The lines can create a triangle')
else:
    print('The lines can\'t create a triangle')