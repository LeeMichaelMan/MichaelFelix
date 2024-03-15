class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Транспорт рухається зі швидкістю {self.speed} км/год.")


class Car(Transport):
    def __init__(self, speed, car_type):
        super().__init__(speed)
        self.car_type = car_type

    def move(self):
        super().move()
        print(f"Тип машини: {self.car_type}")


class Plane(Transport):
    def __init__(self, speed, plane_type):
        super().__init__(speed)
        self.plane_type = plane_type

    def move(self):
        super().move()
        print(f"Тип літака: {self.plane_type}")


car = Car(100, "Легковий")
plane = Plane(800, "Пасажирський")

car.move()
plane.move()
