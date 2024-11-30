from function import *

def main():
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
# файл с товаром
file_name = "products.txt"
try:
    with open('products.txt', "x") as file:
        file.write("Футбольный мяч,1500,10\n")
        file.write("Теннисная ракетка,2500,5\n")
        file.write("Спортивная бутылка,500,20\n")
        file.write("Фитнес-коврик,1200,8\n")
        file.write("Кросовки,4000,30\n")
        file.write("Кеды,5000,35\n")
except FileExistsError:
    pass
# файл с данными для входа
try:
    with open("users.txt", "x") as file:
        file.write("admin,1234\n")
        file.write("user,pass\n")
except FileExistsError:
    pass

# запуск программы
if main():
    store = Cashier(file_name)
    store.main()

if __name__ == "__main__":
    main()