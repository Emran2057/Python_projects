try:
    n = int(input("Enter the number of apple Kamal got: "))
    mn = int(input("Enter the value for mn: "))
    mx = int(input("Enter the value for mx: "))
except ValueError:
    print("Please enter the integer value.")
    exit()

if mn >= mx:
    print("This is not a range so please enter the greater value for mx.")
else:
    for i in range(mn, mx+1):
        if n % i == 0:
            print(f"{i} is divisor of {n}.")
        else:
            print(f"{i} is not divisor of {n}.")
