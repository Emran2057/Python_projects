import datetime

def getdate():
    return datetime.datetime.now()


def log(name, ex_or_fo):
    if ex_or_fo == 1:
        if name == "Sakar":
            f = open("Sakar_exercise.txt")
            content = f.read()
            print(content)
            f.close()
        elif name == "Nawodit":
            f = open("Nawodit_exercise.txt")
            content = f.read()
            print(content)
            f.close()
        elif name == "Aman":
            f = open("Aman_exercise.txt")
            content = f.read()
            print(content)
            f.close()
        else:
            print("Invalid Name. Please try Sakar, Nawodit and Aman only.")

    elif ex_or_fo == 2:
        if name == "Sakar":
            f = open("Sakar_food.txt")
            content = f.read()
            print(content)
            f.close()
        elif name == "Nawodit":
            f = open("Nawodit_food.txt")
            content = f.read()
            print(content)
            f.close()
        elif name == "Aman":
            f = open("Aman_food.txt")
            content = f.read()
            print(content)
            f.close()
        else:
            print("Invalid Name. Please try Sakar, Nawodit and Aman only.")

    else:
        print("Invalid Input. Please Enter 1 or 2.")


def retrieve(name, ex_or_fo):
    if ex_or_fo == 1:
        if name == "Sakar":
            f = open("Sakar_exercise.txt", "a")
            name_exercise = input("Which exercise did Sakar did: ")
            name_exercise_withtime = f"[{getdate()}] {name_exercise} \n"
            f.write(name_exercise_withtime)
            f.close()
        elif name == "Nawodit":
            f = open("Nawodit_exercise.txt", "a")
            name_exercise = input("Which exercise did Nawodit did: ")
            name_exercise_withtime = f"[{getdate()}] {name_exercise} \n"
            f.write(name_exercise_withtime)
            f.close()
        elif name == "Aman":
            f = open("Aman_exercise.txt", "a")
            name_exercise = input("Which exercise did Aman did: ")
            name_exercise_withtime = f"[{getdate()}] {name_exercise} \n"
            f.write(name_exercise_withtime)
            f.close()
        else:
            print("Invalid Name. Please try Sakar, Nawodit and Aman only.")

    elif ex_or_fo == 2:
        if name == "Sakar":
            f = open("Sakar_food.txt", "a")
            name_food = input("Which food did Sakar took: ")
            name_food_withtime = f"[{getdate()}] {name_food} \n"
            f.write(name_food_withtime)
            f.close()
        elif name == "Nawodit":
            f = open("Nawodit_food.txt", "a")
            name_food = input("Which food did Nawodit took: ")
            name_food_withtime = f"[{getdate()}] {name_food} \n"
            f.write(name_food_withtime)
            f.close()
        elif name == "Aman":
            f = open("Aman_food.txt", "a")
            name_food = input("Which food did Aman took: ")
            name_food_withtime = f"[{getdate()}] {name_food} \n"
            f.write(name_food_withtime)
            f.close()
        else:
            print("Invalid Name. Please try Sakar, Nawodit and Aman only.")

    else:
        print("Invalid Input. Please Enter 1 or 2.")


while True:
    operation = input('''Enter your choice: 
    log for log,
    retrieve for retrieve,
    exist for exist.  
    ''')

    if operation == "log":
        Exercise_or_Food = int(input('''Enter your choice:
    1 for Exercise,
    2 for Food.
    '''))

        customer_name = input('''Enter your choice:
    for Sakar : Sakar,
    for Nawodit : Nawodit,
    for Aman : Aman
    ''')
        log(customer_name, Exercise_or_Food)

    elif operation == "retrieve":
        Exercise_or_Food = int(input('''Enter your choice:
    1 for Exercise,
    2 for Food.
    '''))

        customer_name = input('''Enter your choice:
    for Sakar : Sakar,
    for Nawodit : Nawodit,
    for Aman : Aman
    ''')
        retrieve(customer_name, Exercise_or_Food)

    elif operation == "exist":
        break

    else:
        print("Invalid input. Please enter log, retrieve or exist.")
        operation = input('''Enter your choice: 
    log for log,
    retrieve for retrieve,
    exist for exist.  
    ''')

        Exercise_or_Food = int(input('''Enter your choice:
    1 for Exercise,
    2 for Food.
    '''))

        customer_name = input('''Enter your choice:
    for Sakar : Sakar,
    for Nawodit : Nawodit,
    for Aman : Aman
    ''')
