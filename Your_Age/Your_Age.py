user_input = int(input("Enter your age or year of birth: "))
age = 2023 - user_input


def future_age_prediction():
    particular_year = int(input("Enter the year you want to know your age at that year."))
    future_age = (particular_year-2023)+age
    fut_age = (particular_year-2023)+user_input
    if 0 < fut_age < 101:
        print(f"Your age will be {fut_age} in {particular_year}.")
    elif 100 < fut_age < 200:
        print(f"Your age will be {fut_age} in {particular_year}.")
        print("You are the oldest person alive.")
    elif 0 < future_age < 101:
        print(f"Your age will be {future_age} in {particular_year}.")
    elif 100 < future_age < 200:
        print(f"Your age will be {future_age} in {particular_year}.")
        print("You are the oldest person alive.")
    else:
        print("Please! Enter the correct year to check the age.")


if 0 < user_input < 100:
    current_age = 100 - user_input
    print(f"Your current age is {user_input} year old in 2023.")
    print(f"You turn 100 year old after {current_age} year from 2023.")
    print(f"You turn 100 year old in {2023 + current_age}.")
    future_age_prediction()
elif 99 < user_input < 150:
    print("You already cross 100 years.")
    future_age_prediction()
elif 1922 < user_input < 2024:
    print(f"Your current age is {age} year old in 2023.")
    print(f"You turn 100 year old after {100 - age} year from 2023.")
    print(f"You turn 100 year old in {user_input + 100}.")
    future_age_prediction()
elif user_input == 0 or user_input >= 2024:
    print("You are not born yet.")
else:
    print("Please! Enter valid age or year.")
