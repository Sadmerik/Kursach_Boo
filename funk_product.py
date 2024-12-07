class Product:
    # описание товара
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)
    # вывод имени цены и колличества товара
    def __str__(self):
        return  f"{self.name} - {self.price}₽ (В наличии: {self.quantity}"
