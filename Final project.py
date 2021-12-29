num = input("Enter a number:")
while len(num) != 6 or not num.isdecimal():
    num = input("Enter a number:")
lst = [int(character) for character in num]
print(f"{num}\n{lst}")
operators = ['+', '-','*','/']
# Where op stands for math operator.
for op1 in ['+', '-']:
    for op2 in operators:
        for op3 in operators:
            for op4 in operators:
                for op5 in operators:
                    for op6 in operators:
                        print(f'{op1}{lst[0]}{op2}{lst[1]}{op3}{lst[2]}{op4}{lst[3]}{op5}{lst[4]}{op6}{lst[5]}')

