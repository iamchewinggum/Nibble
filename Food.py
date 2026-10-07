#class
class Food:
    #constuctor 
    def __init__(self, name, serving_size, calories_per_serving, protein_per_serving, carbs_per_serving, fat_per_serving):
        self.name = name
        self.serving_size = serving_size
        self.calories_per_serving = calories_per_serving
        self.protein_per_serving = protein_per_serving
        self.carbs_per_serving = carbs_per_serving
        self.fat_per_serving = fat_per_serving
    #class function 
    def food_info(self):
        info = {
            "ate": self.name,
            "Serving size": self.serving_size,
            "Calories": self.calories_per_serving,
            "Protein": self.protein_per_serving,
            "Carbs": self.carbs_per_serving,
            "Fats": self.fat_per_serving,
        }
        for label, value in info.items():
            print(f"{label}: {value}")
