def is_palindrome(n):
    return str(n) == str(n)[::-1]


def not_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n


number_test = int(input("Enter the number of test case you need: "))
numbers = []
for i in range(number_test):
    number = int(input("Enter the number: "))
    numbers.append(number)

for i in range(number_test):
    print(f"Next palindrome is {numbers[i]} is {not_palindrome(numbers[i])}")

