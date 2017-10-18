import  sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('test.db', check_same_thread=False)

    def comparePW(self, pw):
        cur = self.conn.cursor()
        sql = "SELECT * FROM user WHERE pw = " + pw
        cur.execute(sql)
        return cur.fetchall().__len__()

    def createTable(self):
        cur = self.conn.cursor()
        sql = "CREATE TABLE customer(id integer primary key autoincrement, name text not null, category integer, region text)"
        cur.execute(sql)
        self.conn.commit()

    def insertData(self):
        cur = self.conn.cursor()
        sql = "insert into customer(name, category, region) values (?, ?, ?)"
        cur.execute(sql, ('강태영', 1, '부산'))
        self.conn.commit()

    def createAlaramTable(self):
        cur = self.conn.cursor()
        sql = "CREATE TABLE alaram(no integer primary key autoincrement, subject text not null, time text not null)"
        cur.execute(sql)
        self.conn.commit()

    def insertAlaramData(self):

        data = ( ('기상 시간', '07:00'), ('출근 시간', '08:00') )

        cur = self.conn.cursor()
        sql = "INSERT INTO alaram(subject, time) VALUES(?, ?)"
        cur.executemany(sql, data)

        self.conn.commit()

    def selectAlaramData(self):

        cur = self.conn.cursor()
        sql = "SELECT * FROM alaram"
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(row)

    def deleteAlaramData(self):
        cur = self.conn.cursor()
        sql = "DELETE FROM alaram WHERE no > 2"

        result = cur.execute(sql)
        print(result)

        self.conn.commit()

    def updateAlaramData(self):
        cur = self.conn.cursor()
        sql = "UPDATE alaram Set subject = '기상 시간' WHERE no = 1"
        cur.execute(sql)

        self.conn.commit()

    def createUserTable(self):
        cur = self.conn.cursor()
        sql = "CREATE TABLE user(no integer primary key autoincrement, name text not null, pw text not null)"
        cur.execute(sql)
        self.conn.commit()

    def insertUserTable(self):
        cur = self.conn.cursor()
        sql = "INSERT INTO user(name, pw) VALUES(?, ?)"
        cur.execute(sql, ('강태영', '1234'))
        self.conn.commit()


    def selectUserTable(self):
        cur = self.conn.cursor()
        sql = "SELECT * FROM user"
        cur = self.conn.execute(sql)

        rows = cur.fetchall()

        for row in rows:
            print(row)


if __name__ == "__main__":
    print("Hi!")