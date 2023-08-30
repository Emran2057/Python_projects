import random
list_game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
chance = 0
while chance < 10:
    player_choice = input('''Play Guessing game number between 1 to 9...
    ''')
    choice = random.choice(list_game)
    if choice == player_choice:
        print("You won.")
        print(f"{chance} number of chance you take to win.")
        break
    elif choice != player_choice:
        print(f"{9-chance} number chance you left.")
    else:
        print("Invalid input.")
    chance += 1

if chance == 10:
    print("Game Over")