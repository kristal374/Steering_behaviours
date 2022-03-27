import math

class Vector:
    def __init__(self, x=0.0, y=0.0):
        """Хранит данные вектора"""
        self.x = x
        self.y = y

    def lenght(self):
        """Возвращает длинну вектора"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        """Возвращает новый нормализованый вектор"""
        lenght = self.lenght()
        if lenght != 0:
            x = self.x / lenght
            y = self.y / lenght
            return Vector(x, y)
        else:
            return Vector()


def vector_sum(vector_1: Vector, vector_2: Vector) -> Vector:
    """Суммирует два вектора"""
    x = vector_1.x + vector_2.x
    y = vector_1.y + vector_2.y
    return Vector(x, y)


def vector_sub(vector_1: Vector, vector_2: Vector) -> Vector:
    """Вычитает два вектора"""
    x = vector_1.x - vector_2.x
    y = vector_1.y - vector_2.y
    return Vector(x, y)


def vector_mult(vector: Vector, multiplicator: float) -> Vector:
    """Умножает вектор на число"""
    x = vector.x * multiplicator
    y = vector.y * multiplicator
    return Vector(x, y)


def vector_div(vector: Vector, divisor: float) -> Vector:
    """Делит вектор на число"""
    x = vector.x / divisor
    y = vector.y / divisor
    return Vector(x, y)
