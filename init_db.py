import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="flaskblog"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS posts")
mycursor.execute("CREATE TABLE posts ( id INT PRIMARY KEY AUTO_INCREMENT, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, title TEXT NOT NULL, content TEXT NOT NULL )")

mycursor.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ('First Post', 'Content for the first post')
)

mycursor.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ('Second Post', 'Content for the second post')
)

mydb.commit()
mydb.close()