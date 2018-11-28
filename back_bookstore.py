import sqlite3

def init_table():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert_data(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    sql_command = """INSERT INTO book VALUES (NULL,"{ti}","{au}",{ye},{isb})""".format(ti=title,au=author,ye=year,isb=isbn)
    cur.execute(sql_command)
    conn.commit()
    conn.close()

def print_data():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    result = cur.fetchall()
    #for r in result:
    #    print(r)
    conn.close()
    return result

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM book WHERE title="{ti}" OR author="{au}" OR year="{ye}" OR isbn="{isb}" """.format(ti=title,au=author,ye=year,isb=isbn))
    result = cur.fetchall()
    #for r in result:
    #    print(r)
    conn.close()
    return result

def delete_data(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    sql_command = """DELETE FROM book WHERE id="{i}" """.format(i=id)
    cur.execute(sql_command)
    conn.commit()
    conn.close()

def update_data(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    sql_command = """UPDATE book SET title="{ti}", author="{au}", year="{ye}", isbn="{isb}" WHERE id="{i}" """.format(ti=title,au=author,ye=year,isb=isbn,i=id)
    cur.execute(sql_command)
    conn.commit()
    conn.close()

def test():
    print("works")

def main():
    init_table()
    insert_data("the earth","Melani Martinez",2018,2452443534)
    # for r in print_data():
    #     print(r)
    # for r in search(isbn="2452443534"):
    #     print(r)
    #delete_data(2)
    # for r in print_data():
    #     print(r)
    # update_data(1, 'the sea', 'Nicolas Nosenzo', 2000, 2452443534)
    # for r in print_data():
    #     print(r)


if __name__ == '__main__':
    main()
