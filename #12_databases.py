# ========================= Databases =========================
import sqlite3

db = sqlite3.connect("app.db")

db.execute("CREATE TABLE IF NOT EXISTS users (user_id integer, name text, email text)")

cr = db.cursor()

# cr.execute("INSERT INTO users (user_id, name, email) VALUES (1, 'Yehya', 'y@yahoo.com')")
# cr.execute("INSERT INTO users (user_id, name, email) VALUES (2, 'Alaa', 'a@yahoo.com')")
# cr.execute("INSERT INTO users (user_id, name, email) VALUES (3, 'Ebrahim', 'e@yahoo.com')")

cr.execute("UPDATE users SET name = 'Mazen' WHERE user_id = 1")
cr.execute("UPDATE users SET name = 'Maher' WHERE user_id = 2")
cr.execute("UPDATE users SET name = 'Ahmad' WHERE user_id = 3")


cr.execute("DELETE FROM users WHERE user_id =1")


cr.execute("SELECT * FROM users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())


print(cr.fetchall())

# print(cr.fetchmany(2))


db.commit()

db.close()

