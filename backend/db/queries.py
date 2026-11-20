from db.connection import connect
from Food import Food
from FoodEntry import FoodEntry
from Meal import Meal
from User import User


def save_user(user):
    with connect() as conn:
        conn.execute(
            "INSERT INTO users (name, age, sex, height, weight, activity) "
            "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (name) DO NOTHING",
            (user.name, user.age, user.sex, user.height, user.weight, user.activity),
        )


def save_meal(user, meal):
    with connect() as conn:
        user_id = conn.execute(
            "SELECT id FROM users WHERE name = %s", (user.name,)
        ).fetchone()[0]

        meal_id = conn.execute(
            "INSERT INTO meals (user_id, name, meal_type, date_ate, time_ate) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (user_id, meal.name, meal.meal_type, meal.date_ate, meal.time_ate),
        ).fetchone()[0]

        for entry in meal.entries:
            f = entry.food
            conn.execute(
                "INSERT INTO meal_entries (meal_id, food_name, serving_size, calories, "
                "protein, carbs, fat, amount_ate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (meal_id, f.name, f.serving_size, f.calories_per_serving,
                 f.protein_per_serving, f.carbs_per_serving, f.fat_per_serving,
                 entry.amount_ate),
            )


def load_user(name):
    """Return a User (with their saved meals) or None if the name isn't found."""
    with connect() as conn:
        row = conn.execute(
            "SELECT name, age, sex, height, weight, activity FROM users WHERE name = %s",
            (name,),
        ).fetchone()
        if row is None:
            return None

        user = User(*row)

        meals = conn.execute(
            "SELECT m.id, m.name, m.meal_type, m.date_ate, m.time_ate "
            "FROM meals m JOIN users u ON u.id = m.user_id "
            "WHERE u.name = %s ORDER BY m.id",
            (name,),
        ).fetchall()

        for meal_id, mname, mtype, date_ate, time_ate in meals:
            meal = Meal(mname, mtype, date_ate, time_ate)
            entries = conn.execute(
                "SELECT food_name, serving_size, calories, protein, carbs, fat, amount_ate "
                "FROM meal_entries WHERE meal_id = %s ORDER BY id",
                (meal_id,),
            ).fetchall()
            for fname, size, cal, pro, carb, fat, amount in entries:
                meal.add_entry(FoodEntry(Food(fname, size, cal, pro, carb, fat), amount))
            user.book[meal_id] = meal
            user.next_key = meal_id + 1

        return user