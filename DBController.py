import  sqlite3

conn = sqlite3.connect('test.db')


def createTable():
    cur = conn.cursor()
    sql = "CREATE TABLE customer(id integer primary key autoincrement, name text not null, category integer, region text)"
    cur.execute(sql)
    conn.commit()

def insertData():
    cur = conn.cursor()
    sql = "insert into customer(name, category, region) values (?, ?, ?)"
    cur.execute(sql, ('강태영', 1, '부산'))
    conn.commit()
def test():

    cur = conn.cursor()

    cur.execute("select * from customer")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    test()