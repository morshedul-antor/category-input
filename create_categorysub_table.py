import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="categories"
)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE sub_category (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, category_id INT NOT NULL)")

print('Table created...')
