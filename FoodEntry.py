class FoodEntry:
    def __init__(self, food, amount_ate):
        self.food = food
        self.amount_ate = amount_ate

    def calculate_macros(self):
        ratio = self.amount_ate / self.food.serving_size
        return {
            "calories": ratio * self.food.calories_per_serving,
            "protein": ratio * self.food.protein_per_serving,
            "carbs": ratio * self.food.carbs_per_serving,
            "fat": ratio * self.food.fat_per_serving,
        }

    def print_macros(self):
        for label, value in self.calculate_macros().items():
            print(f"{label.capitalize()}: {value:.1f}")


            