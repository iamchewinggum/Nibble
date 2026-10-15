from Food import Food

foods = []  

while True:
    print("\n1: Create Food")
    print("2: Show all foods")
    print("5: Quit")

    choice = input("Enter a number: ")

    if choice == "1":
        print("*\n")
        name = input("Name: ")
        calories = input("Calories: ")
        protein = input("Protein: ")
        carbs = input("Carbs: ")
        fat = input("Fat: ")
        sugar = input("Sugar: ")

        new_food = Food(name, 
                        calories, 
                        protein, 
                        carbs, 
                        fat, 
                        sugar)  # new object each time
        
        foods.append(new_food)                                       # save it in the list
        print(f"Added {name}!")
        print("barlitos\n")
    elif choice == "2":

        for food in foods:
            print("*\n")
            food.food_info()
            print("*\n")

    elif choice == "5":


        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")