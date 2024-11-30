class User:
    """Класс для описания пользователя."""
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Product:
    """Класс для описания товара."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} - {self.price}₽ (в наличии: {self.quantity})"


class SportsStoreCashier:
    """Автоматизированное рабочее место кассира спортивного магазина."""

    def __init__(self, file_name):
        self.file_name = file_name
        self.products = []
        self.cart = []
        self.load_products()

    def load_products(self):
        """Считывает товары из файла."""
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
                for line in lines:
                    name, price, quantity = line.strip().split(",")
                    self.products.append(Product(name, price, quantity))
        except FileNotFoundError:
            print("Ошибка: Файл с товарами не найден.")
        except Exception as e:
            print("Ошибка при чтении файла:", e)

    def save_products(self):
        """Сохраняет текущие остатки товаров в файл."""
        with open(self.file_name, "w") as file:
            for product in self.products:
                file.write(f"{product.name},{product.price},{product.quantity}\n")

    def show_products(self):
        """Показывает список доступных товаров."""
        print("\nДоступные товары:")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product}")

    def add_to_cart(self, product_index, quantity):
        """Добавляет товар в корзину."""
        if product_index < 1 or product_index > len(self.products):
            print("Ошибка: Неверный номер товара.")
            return

        product = self.products[product_index - 1]
        if quantity > product.quantity:
            print(f"Ошибка: Недостаточно товара. Доступно: {product.quantity}")
        else:
            product.quantity -= quantity
            self.cart.append(Product(product.name, product.price, quantity))
            print(f"Добавлено в корзину: {product.name} x {quantity}")

    def show_cart(self):
        """Показывает содержимое корзины."""
        if not self.cart:
            print("\nКорзина пуста.")
        else:
            print("\nТовары в корзине:")
            total = 0
            for item in self.cart:
                print(f"{item.name} - {item.price}₽ x {item.quantity}")
                total += item.price * item.quantity
            print(f"\nИтого: {total}₽")

    def checkout(self):
        """Завершает покупку."""
        if not self.cart:
            print("Корзина пуста. Завершение покупки невозможно.")
        else:
            self.show_cart()
            print("\nПокупка завершена. Спасибо за покупку!")
            self.cart = []
            self.save_products()

    def run(self):
        """Основной цикл программы."""
        while True:
            command = input("\nВведите команду (Menu для отображения меню, Exit для выхода): ").strip()
            if command.lower() == "menu":
                print("\nМеню:")
                print("1. Показать товары")
                print("2. Добавить товар в корзину")
                print("3. Показать корзину")
                print("4. Завершить покупку")
                print("5. Выйти")

                choice = input("Выберите действие: ").strip()
                if choice == "1":
                    self.show_products()
                elif choice == "2":
                    self.show_products()
                    try:
                        product_index = int(input("Введите номер товара: "))
                        quantity = int(input("Введите количество: "))
                        self.add_to_cart(product_index, quantity)
                    except ValueError:
                        print("Ошибка: Введите числовое значение.")
                elif choice == "3":
                    self.show_cart()
                elif choice == "4":
                    self.checkout()
                elif choice == "5":
                    print("До свидания!")
                    break
                else:
                    print("Ошибка: Неверный выбор. Попробуйте снова.")
            elif command.lower() == "exit":
                print("До свидания!")
                break
            else:
                print("Неизвестная команда. Введите 'Menu' для отображения меню или 'Exit' для выхода.")


def login():
    """Вход в систему по логину и паролю."""
    try:
        with open("users.txt", "r") as file:
            users = {}
            for line in file.readlines():
                username, password = line.strip().split(",")
                users[username] = password

        print("Пожалуйста, войдите в систему.")
        for _ in range(3):  # Ограничение на 3 попытки входа
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if username in users and users[username] == password:
                print(f"Добро пожаловать, {username}!")
                return True
            else:
                print("Неверный логин или пароль.")
        print("Вы исчерпали все попытки входа.")
        return False
    except FileNotFoundError:
        print("Ошибка: Файл с пользователями не найден.")
        return False


# Создаем файл с товарами, если он не существует
file_name = "products.txt"
try:
    with open(file_name, "x") as file:
        file.write("Футбольный мяч,1500,50\n")
        file.write("Теннисная ракетка,2500,50\n")
        file.write("Спортивная бутылка,500,20\n")
        file.write("Фитнес-коврик,1200,50\n")
        file.write("Кросовки,4000,30\n")
        file.write("Кеды,5000,35\n")

except FileExistsError:
    pass

# Создаем файл с пользователями, если он не существует
try:
    with open("users.txt", "x") as file:
        file.write("admin,1234\n")
        file.write("user,pass\n")
except FileExistsError:
    pass

# Вход и запуск программы
if login():
    store = SportsStoreCashier(file_name)
    store.run()
