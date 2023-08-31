import random

a = int(input("Enter the first number to fixed a range: "))
b = int(input("Enter the second number to fixed a range: "))
player1_number = random.randint(a, b)
player2_number = random.randint(a, b)


def no_of_chance(num1, num2, num3):
    player_chance = 1
    while True:
        guess_num = int(input(f"Guess a number between {num1} and {num2}: "))
        if guess_num == num3:
            print("You won.")
            print(f"Number of guess you took to finish is {player_chance}")
            break

        elif guess_num != num3:
            if guess_num > num3:
                print(f"Your guess number is greater than number so choose {guess_num} smaller number.")
                player_chance += 1

            elif guess_num < num3:
                print(f"Your guess number is smaller than number so choose {guess_num} greater number.")
                player_chance += 1
    return player_chance


while True:
    print("Player 1 turn.")
    player1 = no_of_chance(a, b, player1_number)
    print("Player 2 turn.")
    player2 = no_of_chance(a, b, player2_number)
    if player1 > player2:
        print("Player 2 win.")
    elif player1 < player2:
        print("Player 1 win.")
    else:
        print("Tie")
    print(f"The number for player 1 was {player1_number}.")
    print(f"The number for player 2 was {player2_number}.")
    break

