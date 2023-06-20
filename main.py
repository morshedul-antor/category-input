import mysql.connector

i = 1


def insert(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biztrade"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO categories (name) VALUES (%s )"
    val = ([name])

    mycursor.execute(sql, val)
    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted.")
    i += 1


def app():
    with open('category.txt') as f:
        lines = f.readlines()

        for line in lines:
            insert(line.strip())


if __name__ == '__main__':
    app()
