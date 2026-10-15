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
    def add_food(self, foodEntry):
        
        self.book[self.next_key] = foodEntry
 
        print(self.next_key, ":" , foodEntry.food.name)

        self.next_key =  self.next_key + 1





    #class function 
    def remove_food(self, key):
        if key in self.book:
            del self.book[key]
            print(f"Food entry '{key}' removed successfully.")
        else:
            print(f"Food entry '{key}' not found.")
        

    #class function 
    def edit_food(self, key, foodEntry):
        if key in self.book:
            self.book[key] = foodEntry
            print(f"Food entry '{key}' updated successfully.")
        else:
            print(f"Food entry '{key}' not found.")
        
    #class function 
    def view_book(self):
        if not self.book:
            print("No food entries found.")
        else:
            for key, foodEntry in self.book.items():
                print(f"Key: {key}, Food: {foodEntry.food.name}, Amount Ate: {foodEntry.amount_ate}, Meal Type: {foodEntry.meal_type}, Date Ate: {foodEntry.date_ate}, Time Ate: {foodEntry.time_ate}")