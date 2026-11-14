from datetime import datetime

from Food import Food
from FoodEntry import FoodEntry
from Meal import Meal
from User import User


def get_number(prompt):
    """Keep asking until the user types a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a number that is 0 or higher.")
                continue
            return value
        except ValueError:
            print("Please enter a number.")


def log_meal(user):
    now = datetime.now()

    meal_name = input("\nMeal name (e.g. Salad, Banana): ")
    meal_type = input("Meal type (Breakfast/Lunch/Dinner/Snack): ")
    meal = Meal(meal_name, meal_type,
                now.strftime("%Y-%m-%d"), now.strftime("%H:%M"))

    while True:
        print("\n--- Add an item ---")
        name = input("Item name: ")
        serving_size = get_number("Serving size (grams): ")
        calories = get_number("Calories per serving: ")
        protein = get_number("Protein per serving: ")
        carbs = get_number("Carbs per serving: ")
        fat = get_number("Fat per serving: ")
        amount = get_number("How much did you eat (grams)? ")

        food = Food(name, serving_size, calories, protein, carbs, fat)
        meal.add_entry(FoodEntry(food, amount))

        if input("Add another item to this meal? (y/n): ").lower() != "y":
            break

    user.add_meal(meal)
    print("\nLogged!")
    meal.print_summary()


# --- program starts here ---
print("Welcome to Nibble! Let's set up your profile.")
user = User(
    input("Name: "),
    get_number("Age: "),
    input("Sex: "),
    get_number("Height (cm): "),
    get_number("Weight (kg): "),
    input("Activity level: "),
)

while True:
    print("\n1: Log a meal")
    print("2: View my book")
    print("5: Quit")

    choice = input("Enter a number: ")

    if choice == "1":
        log_meal(user)
    elif choice == "2":
        user.view_book()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")