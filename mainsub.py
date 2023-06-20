import mysql.connector

i = 1


def insert(name, category_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="categories"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO sub_category (name, category_id) VALUES (%s, %s )"
    val = (name, category_id)

    mycursor.execute(sql, val)
    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted.")
    i += 1


def app():
    with open('categorysub.txt') as f:
        lines = f.readlines()

        for line in lines:
            splt = line.split('|')
            insert(splt[0].strip(), int(splt[1].strip()))


if __name__ == '__main__':
    app()
