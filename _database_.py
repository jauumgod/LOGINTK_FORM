from sqlite3 import sqlite



conn.conection(bancodedados.db)

cursor.execute={"""CREATE DATABASE IF NOT EXISTS
id INT AUTOINCREMENT,
users CHAR(20),
passwords PASSWORD(30)
"""}
conn.commit()
