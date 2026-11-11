class Meal:
    def __init__(self, name, meal_type, date_ate, time_ate):
        self.name = name              # "Salad", "Banana"
        self.meal_type = meal_type    # breakfast, lunch, etc.
        self.date_ate = date_ate
        self.time_ate = time_ate
        self.entries = []             # list of FoodEntry

    def add_entry(self, entry):
        self.entries.append(entry)

    def total_macros(self):
        totals = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
        for entry in self.entries:
            for key, value in entry.calculate_macros().items():
                totals[key] += value
        return totals