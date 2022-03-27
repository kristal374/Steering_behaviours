import math as _math

class Objects:
    def __init__(self, grad=0, cords=(250, 250), size=7):
        """Хранит текущее состояние графического объекта"""
        self.__cord = cords
        self.__grad = _math.radians(-grad)
        self.__size = size
        self.__obj = None

    def position(self, targets):
        """Обновляет текущие данные графического объекта"""
        if targets != self.__cord:
            self.__grad = -(_math.atan2(self.__cord[0]-targets[0], self.__cord[1]-targets[1])+_math.radians(90))
            self.__cord = targets

    def cords(self, alpha, size):
        """Возвращает координаты для построения графического примитива"""
        return _math.cos(alpha)*size+self.__cord[0], _math.sin(alpha)*size+self.__cord[1]

    def draw(self, canv, target, color='red'):
        """Создаёт графический примитив на холсте canv"""
        self.position(target)
        canv.delete(self.__obj)
        coord = [
            (self.cords(self.__grad, self.__size), self.cords(self.__grad, self.__size)),
            (self.cords(self.__grad + _math.radians(135), self.__size), self.cords(self.__grad + _math.radians(135), self.__size)),
            (self.cords(self.__grad, -self.__size * 0.25), self.cords(self.__grad, -self.__size * 0.25)),
            (self.cords(self.__grad - _math.radians(135), self.__size), self.cords(self.__grad - _math.radians(135), self.__size))
        ]
        self.__obj = canv.create_polygon(coord, fill=color)
