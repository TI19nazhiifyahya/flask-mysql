# import sqlite3
import mysql.connector

# connection = sqlite3.connect('database.db')
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "database"
)

# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()
cur.execute("DROP TABLE IF EXISTS posts")
cur.execute("CREATE TABLE posts ( id INT PRIMARY KEY AUTO_INCREMENT, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, title TEXT NOT NULL, content TEXT NOT NULL )")
cur.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post')
)

cur.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ('Second Post', 'Content for the second post')
)

connection.commit()
connection.close()