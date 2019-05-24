import sqlite3
from dobryva import Dobruva


class Data:
    def __init__(self, namedatabase, table):
        self.namedatabase = namedatabase
        self.table = table
        self.connect = sqlite3.connect(self.namedatabase)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM {}".format(self.table))
        self.arr = self.cursor.fetchall()
        self.array = []
        for i in self.arr:
            self.array.append(Dobruva(i[0], i[1], i[2]))

    def FullDataDobruv(self):
        print("id|Назва|Кількість|")
        for i in self.array:
            i.print()

    def addOtherDobruva(self, name, amount):
        self.array.append(Dobruva(len(self.array), name, int(amount)))

    def addSameDobruva(self):
        print("Виберіть що ви хочете добавити:")
        self.FullDataDobruv()
        plus = int(input())
        if plus == 1:
            temp = input("-->")
            self.array[1].setAmount += int(temp)
        if plus == 2:
            temp = input("-->")
            self.array[2].setAmount += int(temp)
        if plus == 3:
            temp = input("-->")
            self.array[3].setAmount += int(temp)
        if plus == 4:
            temp = input("-->")
            self.array[4].setAmount += int(temp)
        if plus == 5:
            temp = input("-->")
            self.array[5].setAmount += int(temp)

    def remuveSameDobruva(self):
        print("Виберіть що ви хочете забрати:")
        self.FullDataDobruv()
        plus = int(input())
        if plus == 1:
            temp = input("-->")
            self.array[1].setAmount -= int(temp)
        if plus == 2:
            temp = input("-->")
            self.array[2].setAmount -= int(temp)
        if plus == 3:
            temp = input("-->")
            self.array[3].setAmount -= int(temp)
        if plus == 4:
            temp = input("-->")
            self.array[4].setAmount -= int(temp)
        if plus == 5:
            temp = input("-->")
            self.array[5].setAmount -= int(temp)

    def delDobruva(self, id):
        self.array.pop(int(id) - 1)

    def __del__(self):
        self.cursor.close()
        self.connect.close()


