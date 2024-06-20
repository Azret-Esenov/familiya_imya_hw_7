import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def insert_product(connection, product):
    try:
        sql = '''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def update_product(connection, product):
    try:
        sql = '''
        UPDATE products SET price = ?
        WHERE id = ?
        '''

        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def update1_product(connection, product):
    try:
        sql = '''
        UPDATE products SET quantity = ?
        WHERE id = ?
        '''

        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def delete_product(connection, id):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''

        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(error)


def select_all_product(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


def select_products_by_price_and_quantity(connection):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = connection.cursor()
        cursor.execute(sql,)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


def find_by_word(connection, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR (200) NOT NULL,
    price FLOAT (10, 2) DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection('hw.db')
if my_connection:
    print('Connected successfully to database!')
    # create_table(my_connection, sql_to_create_products_table)
    # insert_product(my_connection, ('Жидкое мыло с запахом ванили', 150, 36))
    # insert_product(my_connection, ('Мыло детское', 100, 21))
    # insert_product(my_connection, ('Колбаса Аброй Говяжья', 250, 51))
    # insert_product(my_connection, ('Колбаса Аброй Салями', 190, 45))
    # insert_product(my_connection, ('Колбаса Останкино Краковская', 300, 89))
    # insert_product(my_connection, ('Батон пшеничный', 20, 48))
    # insert_product(my_connection, ('Батон Балтийский', 30, 57))
    # insert_product(my_connection, ('Напиток DaDaDay апельс', 90, 35))
    # insert_product(my_connection, ('Напиток Garden Вишневый', 80, 58))
    # insert_product(my_connection, ('Вафли Yashar в глазури', 190, 73))
    # insert_product(my_connection, ('Вафли Ата шоколадные', 200, 76))
    # insert_product(my_connection, ('Молоко Белая Река', 90, 42))
    # insert_product(my_connection, ('Молоко Веселый молочник', 100, 18))
    # insert_product(my_connection, ('Сыр Hochland Фетакса', 250, 28))
    # insert_product(my_connection, ('Сыр Emilia Эмилия', 200, 38))
    # update_product(my_connection, ())
    # update1_product(my_connection, ())
    # delete_product(my_connection)
    # select_all_product(my_connection)
    # select_products_by_price_and_quantity(my_connection)
    # find_by_word(my_connection,)
    my_connection.close()
