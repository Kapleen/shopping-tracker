def add_purchase(item, price):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(f"{item} - {price} сум\n")

def show_purchases():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            print("🛒 Ваши покупки:")
            print(file.read())
    except FileNotFoundError:
        print("Нет сохранённых покупок.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить покупку")
        print("2. Показать покупки")
        print("3. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            item = input("Что купили? ")
            price = input("Сколько стоит?(написать в суммах) ")
            add_purchase(item, price)
        elif choice == "2":
            show_purchases()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()