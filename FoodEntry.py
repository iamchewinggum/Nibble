#class name 
class FoodEntry: 
    #constuctor 
    def __init__(self, food, amount_ate, meal_type, date_ate, time_ate):
        self.food = food
        self.amount_ate = amount_ate
        self.meal_type = meal_type
        self.date_ate = date_ate
        self.time_ate = time_ate
    #class functions 
    def calculate_macros(self, food):
        list = (food.calories_per_serving, food.protein_per_serving, food.carbs_per_serving, food.fat_per_serving)

        macros_calulated = [] #list to store macros calulated from math
        
        for macros in list:
          
          macros_calulated.append ((self.amount_ate / food.serving_size) * macros)

        return macros_calulated

    #class functions
    def print_macros(self):
        label = ["Calories", "Protein", "Carbs", "Fat"]
        macros = self.calculate_macros()

        for label, macros in zip(label, macros):
            print(f"{label}: {macros}")


        