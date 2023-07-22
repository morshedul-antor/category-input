import mysql.connector

i = 1


def insert(name, category_id, sub_category_id):
    mydb = mysql.connector.connect(
        host="bizdata.cxr9ckftrymk.ap-southeast-1.rds.amazonaws.com",
        user="biztradeprodu",
        password="h48eUe3jpYjkd982ueje",
        database="biztradeprod"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO sub_sub_categories (name, category_id, sub_category_id) VALUES (%s, %s, %s )"
    val = (name, category_id, sub_category_id)

    mycursor.execute(sql, val)
    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted.")
    i += 1


def app():
    with open('categorysubsub.txt') as f:
        lines = f.readlines()

        for line in lines:
            splt = line.split('|')
            insert(splt[0].strip(), int(splt[1].strip()), int(splt[2].strip()))


if __name__ == '__main__':
    app()
