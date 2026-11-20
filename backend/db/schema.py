from db.connection import connect


def create_tables():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                age DOUBLE PRECISION, sex TEXT,
                height DOUBLE PRECISION, weight DOUBLE PRECISION,
                activity TEXT
            )""")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                name TEXT NOT NULL,
                meal_type TEXT, date_ate TEXT, time_ate TEXT
            )""")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS meal_entries (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                meal_id INTEGER NOT NULL REFERENCES meals(id) ON DELETE CASCADE,
                food_name TEXT NOT NULL,
                serving_size DOUBLE PRECISION, calories DOUBLE PRECISION,
                protein DOUBLE PRECISION, carbs DOUBLE PRECISION,
                fat DOUBLE PRECISION, amount_ate DOUBLE PRECISION
            )""")