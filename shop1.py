import psycopg2

# --- 1. Ulanish
conn = psycopg2.connect(
    dbname="store_db",
    user="postgres",
    password="123",  # o'z parolingizni yozing
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# --- 2. Ma'lumot qo'shish
def add_product(name, price, quantity):
    cur.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
    conn.commit()
    print("Mahsulot qo‘shildi!")

# --- 3. Barcha mahsulotlarni ko‘rish
def view_products():
    cur.execute("SELECT * FROM products;")
    rows = cur.fetchall()
    for r in rows:
        print(r)

# --- 4. Ma'lumot yangilash
def update_product(id, name, price, quantity):
    cur.execute("UPDATE products SET name=%s, price=%s, quantity=%s WHERE id=%s",
                (name, price, quantity, id))
    conn.commit()
    print("Mahsulot yangilandi!")

# --- 5. Ma'lumot o‘chirish
def delete_product(id):    
    cur.execute("DELETE FROM products WHERE id=%s", (id,))
    conn.commit()
    print("Mahsulot o‘chirildi!")

# --- Test uchun
add_product("Olma", 5000, 10)
add_product("Banan", 8000, 5)
view_products()

# --- Yakun
cur.close()
conn.close()
