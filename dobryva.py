
class Dobruva:
    def __init__(self, id, name,  amount):
        self.id = id
        self.name = name
        self.amount = int(amount)

    @property
    def getId(self):
        return int(self.id)

    @property
    def getName(self):
        return self.name

    @property
    def getAmount(self):
        return int(self.amount)


    @getName.setter
    def setName(self, name):
        self.name = str(name)

    @getAmount.setter
    def setAmount(self, amount):
        self.amount = int(amount)


    def print(self):
        print("{} |{}\t\t\t|{}".format(str(self.getId),
                                           self.getName,
                                           self.getAmount))