class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Колір: {self.color}")


car1 = Car("Tesla", "Model X", 2023, "білий")
car2 = Car("BMW", "X5", 2022, "чорний")
car3 = Car("Mercedes-Benz", "S-Class", 2029, "сірий")

car1.display_info()
print()
car2.display_info()
print()
car3.display_info()
