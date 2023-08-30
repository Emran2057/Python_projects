import random

list_game = ["Scissor", "Paper", "Rock"]
chance = 10
no_of_chance = 0
player_point = 0
pc_point = 0
tie_point = 0

while no_of_chance < chance:
    player_choice = input('''Play Scissor, Paper, Rock game...
    Scissor for Scissor,
    Paper for Paper,
    Rock for Rock
    ''')
    pc_choice = random.choice(list_game)
    if pc_choice == "Scissor" and player_choice == "Paper":
        print("You lose.")
        pc_choice += 1
    elif pc_choice == "Paper" and player_choice == "Scissor":
        print("You win.")
        player_point += 1
    elif pc_choice == "Scissor" and player_choice == "Rock":
        print("You win.")
        player_point += 1
    elif pc_choice == "Rock" and player_choice == "Scissor":
        print("You lose.")
        pc_point += 1
    elif pc_choice == "Paper" and player_choice == "Rock":
        print("You lose.")
        pc_point += 1
    elif pc_choice == "Rock" and player_choice == "Paper":
        print("You win.")
        player_point += 1
    elif pc_choice == player_choice:
        print("Tie")
        tie_point += 1
    else:
        print("Invalid input")
    no_of_chance += 1
    print(f"Player points: {player_point}")
    print(f"PC points: {pc_point}")
    print(f"Tie points: {tie_point}")
    print(f"Number of Chance left : {chance-no_of_chance}")

if pc_point > player_point:
    print("\n Final Scores.")
    print("PC won.")
    print(f"Player points: {player_point}")
    print(f"PC points: {pc_point}")
    print(f"Tie points: {tie_point}")
elif pc_point < player_point:
    print("\n Final Scores.")
    print("You won.")
    print(f"Player points: {player_point}")
    print(f"PC points: {pc_point}")
    print(f"Tie points: {tie_point}")
elif pc_point == player_point:
    print("\n Final Scores.")
    print("Tie.")
    print(f"Player points: {player_point}")
    print(f"PC points: {pc_point}")
    print(f"Tie points: {tie_point}")
else:
    print("Unexpected error.")