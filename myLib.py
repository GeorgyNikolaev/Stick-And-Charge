import numpy as np


# Класс для хранения двумерного вектора.
class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Длина вектора.
    def get_length(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    # Нормализация.
    def normalizing(self):
        l = self.get_length()
        self.x /= l
        self.y /= l

    # Переопределение функции ошибки.
    def __add__(self, arg):
        return Vector2d(self.x + arg.x, self.y + arg.y)

    # Переопределение обратной операции сложения.
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    # Возвращение вектора в виде массива.
    def get(self):
        return np.array([self.x, self.y])


# Длина вектора.
def lengthVec(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Сила кулона.
def KulonForce(q1, q2, r):
    return (9 * 10**9 * abs(q1) * abs(q2)) / (r * r)


# Подсчет силы кулона для всех кусочков.
def calculateForce(x, dx, qPos, lambd, q, stick, split):
    vectors_ = []
    idOrientation = 1 if (lambd * q > 0) else -1
    for i in range(split):
        length = lengthVec(qPos[0], qPos[1], x, stick[0][1])
        force = KulonForce(q, lambd * dx, length) * idOrientation
        vec = Vector2d(qPos[0] - x, qPos[1] - stick[1][1])
        vec.normalizing()
        vec.x *= force
        vec.y *= force
        vectors_.append(vec)
        x += dx

    return vectors_


# Проверка числа.
def checkNumber(entry):
    isError = False
    try:
        a = eval(entry.get())
    except NameError:
        isError = True
        baseVal = 0.
        entry.delete(0, 'end')
        entry.insert(0, 'Не число')
    except SyntaxError:
        isError = True
        baseVal = 0.
        entry.delete(0, 'end')
        entry.insert(0, 'Не число')
    else:
        baseVal = a

    return baseVal, isError


# Проверка на ноль.
def checkZero(*args):
    for x in args:
        if x == 0:
            return True

    return False






