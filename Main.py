from data import Data

if __name__ == "__main__":
    data = Data('Dobruva.db', 'dobruva')
    choice = 1
    while int(choice) != 6:
        print("Що ви хочете зробити?")
        print("Показати добрива на складі - 1")
        print("Взяти добрива - 2")
        print("Додати інакше добриво - 3")
        print("Додати добриво - 4")
        print("Забрати вид добрива - 5")
        print("Закрити програму - 6")
        choice = input("Зробіть ваш вибір - ")
        print("=====================\n")
        if int(choice) == 1:
            data.FullDataDobruv()
        if int(choice) == 2:
            data.remuveSameDobruva()
        if int(choice) == 3:
            name = input("Назва добрива - ")
            amount = input("Кількість - ")
            data.addOtherDobruva(name, amount)
        if int(choice) == 4:
            data.addSameDobruva()
        if int(choice) == 5:
            id = input("id - ")
            data.delDobruva(id)
        print("\n=====================\n")



