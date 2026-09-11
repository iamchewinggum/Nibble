class FoodEntry:
    def __init__(self, food, amount_ate, meal_type, date_ate, time_ate):
        self.food = food
        self.amount_ate = amount_ate
        self.meal_type = meal_type
        self.date_ate = date_ate
        self.time_ate = time_ate

    def calculate_macros(self, food):
        list = (self.food.calories_per_serving, self.food.protein_per_serving, self.food.carbs_per_serving)

        for macros in list:
            (self.food.serving_size / macros) * self.amount_ate