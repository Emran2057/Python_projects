def is_palindrome(n):
    return str(n) == str(n)[::-1]


def not_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n


number_test = int(input("Enter the number of elements you want: "))
numbers = []
for i in range(number_test):
    number = int(input("Enter the number: "))
    numbers.append(number)

Palindromify_the_List = []
for i in range(number_test):
    if numbers[i] > 10:
        Palindromify_the_List.append(not_palindrome(numbers[i]))
    else:
        Palindromify_the_List.append(numbers[i])
print(f"Output List is {Palindromify_the_List}")
