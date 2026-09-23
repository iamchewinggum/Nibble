class User:
    def __init__(self, name, age, sex, height, weight, activity):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity = activity

    book = {}

    def add_food(self, foodEntry):
        pass

    def remove_food(self, key, foodEntry):
        if key in self.book:
            del self.book[key]
            print(f"Food entry '{key}' removed successfully.")
        else:
            print(f"Food entry '{key}' not found.")
        


    def edit_food(self, key, foodEntry):
        if key in self.book:
            self.book[key] = foodEntry
            print(f"Food entry '{key}' updated successfully.")
        else:
            print(f"Food entry '{key}' not found.")
        

  def view_book(self):
        if not self.book:
            print("No food entries found.")
        else:
            for key, foodEntry in self.book.items():
                print(f"Key: {key}, Food: {foodEntry.food.name}, Amount Ate: {foodEntry.amount_ate}, Meal Type: {foodEntry.meal_type}, Date Ate: {foodEntry.date_ate}, Time Ate: {foodEntry.time_ate}")