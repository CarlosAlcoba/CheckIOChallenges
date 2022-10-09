user_num = int(input("Enter a positive digit number: "))
first_digit = user_num // 10
second_digit = user_num % 10
product = first_digit * second_digit

print()
print(f"The product of the digits of {user_num} is {product}")