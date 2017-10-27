#coding:utf-8
import sqlite3, json

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('oneroom.db', check_same_thread=False)

    def selectUserName(self):
        cur = self.conn.cursor()
        sql = "SELECT name FROM user WHERE no = 1"
        cur.execute(sql)

        return cur.fetchone()[0]

    def updatePW(self, curpw, chpw):

        cur = self.conn.cursor()
        sql = "SELECT pw FROM user WHERE pw = ?";
        result = cur.execute(sql, [curpw]).fetchall()

        if result.__len__() > 0:
            sql = "UPDATE user SET pw = ? WHERE pw = ?"
            result = cur.execute(sql, (chpw, curpw))
            self.conn.commit()
            return result.rowcount
        else:
            return -1

    def selectPW(self):
        cur = self.conn.cursor()
        sql = "SELECT pw FROM user"
        cur.execute(sql)
        print(cur.fetchall())

    def comparePW(self, pw):

        self.selectPW()

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

    def getAlaramDataNo(self, subject, time):
        cur = self.conn.cursor()
        sql = "SELECT no FROM alaram WHERE subject = ? and time = ?"
        cur.execute(sql, (subject, time))
        result = cur.fetchall()

        return result

    def insertAlaramData(self, subject, time):

        cur = self.conn.cursor()
        sql = "INSERT INTO alaram(subject, time) VALUES(?, ?)"
        result = cur.execute(sql, (subject, time))
        self.conn.commit()

        return result

    def selectAlaramData(self):

        cur = self.conn.cursor()
        sql = "SELECT * FROM alaram"
        cur.execute(sql)
        rows = cur.fetchall()

        result = []
        for row in rows:
            result.append( {'no' : row[0], 'subject' : row[1], 'time' : row[2]} )

        return result

    def deleteAlaramData(self, no):
        cur = self.conn.cursor()
        sql = "DELETE FROM alaram WHERE no = ?"

        result = cur.execute(sql, [no])
        result = result.fetchall()
        self.conn.commit()

        return result.__len__()

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
    db = DBManager()
    # data = db.selectAlaramData()
    # pass