import random

num = random.randint(1, 100)
no_of_chance = 9

for i in range(0, no_of_chance):
    guess_num = int(input("Enter your guess number between 1 and 100: "))
    if guess_num == num:
        print("You won.")
        print(f"Number of guess you took to finish is {i+1}")
        break

    elif guess_num != num:
        if guess_num > num:
            print(f"Your guess number is greater than number so choose {guess_num} smaller number.")
            print(f"Number of chance you left is {8-i}")
            if i == (no_of_chance - 1):
                print("Game Over")

        elif guess_num < num:
            print(f"Your guess number is smaller than number so choose {guess_num} greater number.")
            print(f"Number of chance you left is {8-i}")
            if i == (no_of_chance - 1):
                print("Game Over")