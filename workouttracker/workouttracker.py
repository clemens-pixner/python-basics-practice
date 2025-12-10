def int_ctrl(text):
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Please enter a valid number")

def float_ctrl(text):
    while True:
        try:
            value = float(input(text))
            return value 
        except ValueError:
            print("Please enter a valid number")

def str_ctrl(text):
    while True:
        value = input(text)
        if value.strip() != "":
            return value
        else:
            print("Please enter something")

workout = []
counter = 0

print("Workout Tracker")

menu = """
-----------------------
1) Add Exercise 
2) View Workout 
3) Exit Workout Tracker
-----------------------
"""
print(menu)


while True:
    selection = int_ctrl("What do you want to do (1/2/3)? ")
    if selection == 1:
        while True:
            name = str_ctrl("What exercise did you do? ")
            sets = int_ctrl("How many sets did you do? ")
            reps = int_ctrl("How many reps did you do per set? ")
            weight = float_ctrl("With how much weight? ")

            exercise = {
                "name" : name,
                "sets" : sets,
                "reps" : reps,
                "weight" : weight
            }

            workout.append(exercise)
            print("Exercise added")

            while True:
                keep_going = str_ctrl("Do you want to add another Exercise (y/n)? ").lower()

                if keep_going in ["y", "n"]:
                    break
                else:
                    print("Please choose between (y/n)")
                               
            if  keep_going == "y":
                continue
            else:
                break
                
    elif selection == 2:
        if len(workout) == 0:
            print("No Exercises found")
            continue
        else:
            print("\nWorkout:")
            for ex in workout:
                print(f"\nExercise: {ex['name']}")
                print(f"Sets: {ex["sets"]}")
                print(f"Reps: {ex["reps"]}")
                print(f"Weight: {ex["weight"]}Kg")
                
    else:
        print("Goodbye!")
        break

