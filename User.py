#class
class User:
    #constuctor 
    def __init__(self, name, age, sex, height, weight, activity):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.activity = activity

        self.book = {} #each user has thier own book 
        #also had the book be a dic 
        #since the app will 1st be on the cl
        #will make looking for things faster
        self.next_key = 0

    #book = {} 
    #commented out since doing this
    #would would allow all the users to share the 
    #same book for everyone 


    #functions for the users




    #class function 
    def add_meal(self, meal):
        
        self.book[self.next_key] = meal
 
        print(self.next_key, ":" , meal.name)

        self.next_key += 1





    #class function 
    def remove_meal(self, key):
        if key in self.book:
            del self.book[key]
            print(f"Meal '{key}' removed successfully.")
        else:
            print(f"Meal '{key}' not found.")
        

    #class function 
    def edit_food(self, key, meal):
        if key in self.book:
            self.book[key] = meal
            print(f"Meal '{key}' updated successfully.")
        else:
            print(f"Meal '{key}' not found.")
        
    #class function 
    def view_book(self):
        if not self.book:
            print("No meals found.")
            return
        for key, meal in self.book.items():
            print(f"\nKey: {key}")
            meal.print_summary()