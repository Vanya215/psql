import psycopg2 as ps
from psycopg2 import  sql

name = ''
age = 0
id = 0
run = True
message = 0
change_column = ""
new_data = ""
how_to_change = ""

conn = ps.connect("dbname = 'db' user = 'postgres' host='localhost' password='150403'")

cur = conn.cursor()

while(run):
    print("What you want:\n 1.Print all table\n 2.Add new data to table\n 3.Change data from table\n 4.Delete data from table\n 5.Exit")
    message = int(input())
    if message == 1:
        cur.execute("SELECT * FROM users;")
        print(cur.fetchall())
    if message == 2:
        cur.execute("SELECT id FROM users ORDER BY id ASC;")
        id = cur.fetchall()[len(cur.fetchall())-1]
        id = int(id[0])
        id += 1
        print("Print name")
        name = input()
        print("Print age")
        age = int(input())
        cur.execute("INSERT INTO users VALUES (%s, %s, %s)", (id, name, age))
    if message == 3:
        print("How you want to change\n 1.Change full column\n 2.Change by name\n 3.Change by id")
        message = int(input())
        print("Witch column you want to change (name, age)")
        change_column = input()

        if message == 2:
            print("Whom data you want to change")
            how_to_change = input()
        if message == 3:
            print("Witch id ypu want to change")
            how_to_change = input()

        print("print new data")
        new_data = input()

        if message != 1:
            cur.execute(sql.SQL("UPDATE users SET {} = %s WHERE name = %s").format(sql.Identifier(change_column)), [new_data, how_to_change])
        else:
            cur.execute(sql.SQL("UPDATE users SET {} = %s").format(sql.Identifier(change_column)), [new_data])

    if message == 4:
        print("How you want to delete\n 1.Clear full table\n 2.Delete by name\n 3.Delete by id")
        message = int(input())

        if message == 1:
            cur.execute("DELETE FROM users;")
        if message == 2:
            print("Whom data you want to delete")
            how_to_change = input()
            cur.execute("DELETE FROM users WHERE name = %s;", [how_to_change])
        if message == 3:
            print("Witch id you want to delete")
            how_to_change = input()
            cur.execute("DELETE FROM users WHERE id = %s;", [how_to_change])

    if message == 5:
        conn.commit()
        conn.close()
        run = False