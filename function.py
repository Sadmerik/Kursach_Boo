import os

class User:
    # описание пользователя
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product:
    # описание товара
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)
    #
    def __str__(self):
        return  f"{self.name} - {self.price}₽ (В наличии: {self.quantity}"

class Cashier:
    # функции кассира
    def __init__(self, file_name):
        self.file_name = file_name
        self.products = []
        self.cart = []
        self.load_products()

    # загрузка товара из файла
    def load_products(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
            for line in lines:
                name, price, quantity = line.strip().split(",")
                self.products.append(Product(name, price, quantity))
        except FileNotFoundError:
            print("\033[31m     Error!\nНет файла с товаром\033[0m")
        except Exception as e:
            print("\033[31m     Error!\nФайл не читается\033[0m", e)
    # обновление файла при покупке чего-либо
    def update_products_file(self):
        with open(self.file_name, "w") as file:
            for product in self.products:
                file.write(f"{product.name},{product.price},{product.quantity}\n")
    # показывает меню продуктов
    def show_products(self):
        print("\n\nДоступные товары:")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product}")
    # добавление продуктов в корзину
    def add_to_product_cart(self, product_index, quantity):
        if product_index < 1 or product_index > len(self.products):
            print("\033[31m Ошибка: Неверный номер товара.\033[0m")
            return
        product = self.products[product_index - 1]
        if quantity > product.quantity:
            print(f"\033[31m Ошибка: Недостаточно товара.\033[0m Доступно: {product.quantity}")
        else:
            product.quantity -= quantity
            self.cart.append(Product(product.name, product.price, quantity))
            print(f"Добавлено в корзину: {product.name} x {quantity}")
    # отобразить корзину
    def show_cart(self):
        if not self.cart:
            print("\nКорзина пуста.")
        else:
            print("\nТовары в корзине:")
            total = 0
            for item in self.cart:
                print(f"{item.name} - {item.price}₽ x {item.quantity}")
                total += item.price * item.quantity
            print(f"\nИтого: {total}₽")

    # завершение покупки
    def checkout(self):
            if not self.cart:
                print("Корзина пуста. Завершение покупки невозможно.")
            else:
                self.show_cart()
                print("\nПокупка завершена. Спасибо за покупку!")
                self.cart = []
                self.update_products_file()
    # основная работа
    def main(self):
        while True:
            command = input("\nВведите команду (Menu для отображения меню, Exit для выхода): ").strip()
            if command.lower() == "menu":
                print("\nМеню:")
                print("1. Показать товары")
                print("2. Добавить товар в корзину")
                print("3. Показать корзину")
                print("4. Завершить покупку")
                print("5. Выйти")

                choice = int(input("Выберите действие: ").strip())
                match choice:
                    case 1:
                        self.show_products()
                    case 2:
                        self.show_products()
                        try:
                            product_index = int(input("Введите номер товара: "))
                            quantity = int(input("Введите количество: "))
                            self.add_to_product_cart(product_index, quantity)
                        except ValueError:
                            print("Ошибка: Введите числовое значение.")
                    case 3:
                        self.show_cart()
                    case 4:
                        self.checkout()
                    case 5:
                        print("До свидания!")
                        os.abort()
                    case _:
                        print("Ошибка: Неверный выбор. Попробуйте снова.")
            elif command.lower() == "exit":
                print("До свидания!")
                break
            else:
                print("Неизвестная команда. Введите 'Menu' для отображения меню или 'Exit' для выхода.")

