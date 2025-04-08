'''Multi'''
a = float(input())
b = float(input())
print(f'{a} * {b} = {a*b}')
if a*b == 0:
    print('This number is both positive and negative.')
elif a*b <0:
    print('This number is negative.')
else:
    print('This number is positive.')
