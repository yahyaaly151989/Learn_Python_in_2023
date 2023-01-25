# ========================= Databases =========================
import sqlite3

db = sqlite3.connect("app.db")


cr = db.cursor()

cr.execute("CREATE TABLE IF NOT EXISTS users (user_id integer, name text, email text)")


# users = ["Yehya", "Alaa", "Mona", "Omar", "Noha"]

# for index, value in enumerate(users, 1):
    # cr.execute(f"INSERT INTO users (user_id, name, email) VALUES ({index}, '{value}', '{value[0].lower()}@yahoo.com')")



# cr.execute("UPDATE users SET name = 'Ebrahim' WHERE user_id = 1")
# cr.execute("UPDATE users SET name = 'Yehya' WHERE user_id = 2")
# cr.execute("UPDATE users SET name = 'Mazen' WHERE user_id = 3")
# cr.execute("UPDATE users SET name = 'Noha' WHERE user_id = 4")
# cr.execute("UPDATE users SET name = 'Hiba' WHERE user_id = 5")

cr.execute("DELETE FROM users WHERE user_id = 5")

cr.execute(f"SELECT user_id, name, email FROM users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())


print(cr.fetchall())

# print(cr.fetchmany(5))

db.commit()


db.close()