#if, else statement is used to check validity of a statement.
x=10
y=20
z=30
if x>y:
    print('x is less than y')#must maintain space. if not error will occur.
elif x==y:
    print('x is equal to y')
else:
    print('y  is greater than x')
num=int(input('enter any value'))
n= num%2
if n==0:
    print('number is even')
else:
    print('number is odd')
num1=float(input('give ur number'))
if num1>0:
    print('number is positive')
elif num1==0:
    print('number is zero')
else:
    print('the number is negetive')