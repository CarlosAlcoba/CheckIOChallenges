'''
num = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
total = num + num2
choice = str(input('You want to add another number?(y or n)'))
while choice == 'y':
    if choice == 'y':
        num = float(input('Enter another number:'))
        total += num
    else:
        break
    choice = str(input('You want to add another number?(y or n)'))
print(f'The total is {total}')


# Challenge 045
print('Challenge 045')
total = 0
while total <= 50:
    num = float(input('Enter a number: '))
    total += num
    print(f'The total is {total}')
print(f'The total s {total}')
'''
print(0.2507089375 > 0.250114225)