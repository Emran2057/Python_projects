operation = input('''Choose one sign from below options for doing this operation
for addition : +,
for subtraction : -,
for multiplication : *,
for divide : /,
for power : ^"
Enter what operation you want do with two numbers. ''')

num1 = int(input("Enter your first number-- "))
num2 = int(input("Enter your second number-- "))

if operation == "*":
    if num1 == 45 and num2 == 3:
        print(555)
    else:
        print(num1 * num2)

elif operation == "+":
    if num1 == 56 and num2 == 9:
        print(77)
    else:
        print(num1 + num2)

elif operation == "/":
    if num1 == 56 and num2 == 6:
        print(4)
    else:
        print(num1 / num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "^":
    print(num1 ** num2)

else:
    print("Invalid operator or it is not mentioned in this program.")