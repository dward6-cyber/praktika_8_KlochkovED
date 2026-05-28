import sqlite3

conn = sqlite3.connect('mybase.db')
cursor = conn.cursor()

print("База данных создана и подключена!")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

conn.commit()
print("Таблица users создана!")
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Анна', 25))

users = [
    ('Иван', 30),
    ('Мария', 22),
    ('Петр', 35)
]
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)

conn.commit()
print("Пользователи добавлены!")

cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()

print("\n--- Все пользователи ---")
for user in all_users:
    print(f"id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

cursor.execute('SELECT * FROM users WHERE age > 25')
older_users = cursor.fetchall()

print("\n--- Пользователи старше 25 ---")
for user in older_users:
    print(f"id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

cursor.execute('UPDATE users SET age = age + 1')
conn.commit()

cursor.execute('SELECT * FROM users')
updated_users = cursor.fetchall()

print("\n--- После увеличения возраста ---")
for user in updated_users:
    print(f"id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

cursor.execute('DELETE FROM users WHERE id = ?', (2,))
conn.commit()

cursor.execute('SELECT * FROM users')
remaining_users = cursor.fetchall()

print("\n--- После удаления id=2 ---")
for user in remaining_users:
    print(f"id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER DEFAULT 0
    )
''')

conn.commit()
print("Таблица products создана!")
products_data = [
    ('Яблоки', 50, 100),
    ('Бананы', 80, 50),
    ('Молоко', 70, 30),
    ('Хлеб', 40, 0),
    ('Сыр', 150, 20)
]

cursor.executemany('''
    INSERT INTO products (name, price, quantity) 
    VALUES (?, ?, ?)
''', products_data)

conn.commit()
print("Товары успешно добавлены!")
cursor.execute('SELECT name, price, quantity FROM products')
all_products = cursor.fetchall()

print("\n--- Задание 12: Все товары ---")

for index, product in enumerate(all_products, start=1):
    print(f"{index}. {product[0]} - {product[1]} руб, в наличии: {product[2]}")

cursor.execute('SELECT name FROM products WHERE price < 100')
cheap_products = cursor.fetchall()

print("\n--- Задание 13: Товары дешевле 100 рублей ---")

print(", ".join([prod[0] for prod in cheap_products]))

cursor.execute('SELECT name FROM products WHERE quantity = 0')
out_of_stock = cursor.fetchall()

print("\n--- Задание 14: Товары, которых нет в наличии ---")

print(", ".join([prod[0] for prod in out_of_stock]))

cursor.execute('UPDATE products SET price = price + 10')
conn.commit()

cursor.execute('SELECT name, price, quantity FROM products')
updated_products = cursor.fetchall()

print("\n--- Задание 15: Товары после увеличения цены на 10 руб ---")

for index, product in enumerate(updated_products, start=1):
    print(f"{index}. {product[0]} - {product[1]} руб, в наличии: {product[2]}")

cursor.execute('DELETE FROM products WHERE price > 100')
conn.commit()

print("\nЗадание 16: Товары дороже 100 рублей удалены!")

cursor.execute('ALTER TABLE products ADD COLUMN category TEXT DEFAULT "другое"')
conn.commit()

categories = [
    ('фрукты', 'Яблоки'),
    ('фрукты', 'Бананы'),
    ('молочные', 'Молоко'),
    ('выпечка', 'Хлеб')
]
cursor.executemany('UPDATE products SET category = ? WHERE name = ?', categories)
conn.commit()

cursor.execute('SELECT name, category, price FROM products')
final_check = cursor.fetchall()

print("\n--- Задание 17: Финальный список товаров с категориями ---")
for prod in final_check:
    print(f"Товар: {prod[0]} | Категория: {prod[1]} | Цена: {prod[2]} руб.")

conn.close()
print("\nСоединение с БД полностью закрыто.")
