import myLib
import showTask
import matplotlib.pyplot as plt
from tkinter import *


width = 600
height = 400

# Запуск кода.
def start():
    window.mainloop()


# Функция симуляции, которая выполняется после нажатия на одноименную кнопку.
def clicked():
    # Закрытие предыдущего окна и задание шаблонов.
    plt.close()
    qPos = [0, 0]
    stick = [[0, 0], [10, 0]]
    error = [False] * 6

    # Проверка введенных значений.
    qVal, error[0] = myLib.checkNumber(qEntry)
    lambd, error[1] = myLib.checkNumber(lambdaEntry)
    qPos[0], error[2] = myLib.checkNumber(qPosXEntry)
    qPos[1], error[3] = myLib.checkNumber(qPosYEntry)
    stick[1][0], error[4] = myLib.checkNumber(stickEntry)
    split, error[5] = myLib.checkNumber(splitEntry)

    # Проверка на ошибку.
    if True in error:
        forceText.config(text="Сила = Ошибка")
        return

    # Длина кусочка и начальные координаты.
    dx = (stick[1][0] - stick[0][0]) / split
    start = dx / 2 + stick[0][0]

    # Если был введен ноль, сила кулона не будет высчитываться.
    if not myLib.checkZero(qVal, lambd, dx):
        vectors = myLib.calculateForce(x=start,
                                       dx=dx,
                                       qPos=qPos,
                                       lambd=lambd,
                                       q=qVal,
                                       stick=stick,
                                       split=split)
        resultVec = sum(vectors)
        force = resultVec.get_length()
        resultVec.normalizing()
        resultVec = resultVec.get()
    else:
        force = 0
        resultVec = [0, 0]

    # Изменение силы в окне.
    forceText.config(text="Сила = " + str(force) + " Н")

    # Отрисовка графика.
    fig, ax = plt.subplots()
    showTask.show(ax=ax,
                  stickPos=stick,
                  qPos=qPos,
                  forceVec=resultVec)
    plt.show()


# Задание окна.
window = Tk()
window.title("Task")
window.geometry(str(width) + 'x' + str(height))

qText = Label(window, text="Заряд = ", font=("Arial", 20), justify='center')
qText.grid(column=0, row=0)
qEntry = Entry(window, width=20)
qEntry.insert(0, '2 * 10 ** (-9)')
qEntry.grid(column=1, row=0)

qPosXText = Label(window, text="Позиция заряда по X = ", font=("Arial", 20), justify='left')
qPosXText.grid(column=0, row=1)
qPosXEntry = Entry(window, width=20)
qPosXEntry.insert(0, '5')
qPosXEntry.grid(column=1, row=1)

qPosYText = Label(window, text="Позиция заряда по Y = ", font=("Arial", 20), justify='left')
qPosYText.grid(column=0, row=2)
qPosYEntry = Entry(window, width=20)
qPosYEntry.insert(0, '5')
qPosYEntry.grid(column=1, row=2)

lambdaText = Label(window, text="Линейная плотность = ", font=("Arial", 20), justify='left')
lambdaText.grid(column=0, row=3)
lambdaEntry = Entry(window, width=20)
lambdaEntry.insert(0, '2')
lambdaEntry.grid(column=1, row=3)

stickText = Label(window, text="Длина палки = ", font=("Arial", 20), justify='left')
stickText.grid(column=0, row=4)
stickEntry = Entry(window, width=20)
stickEntry.insert(0, '10')
stickEntry.grid(column=1, row=4)

splitText = Label(window, text="Количество разбиений = ", font=("Arial", 20), justify='left')
splitText.grid(column=0, row=5)
splitEntry = Entry(window, width=20)
splitEntry.insert(0, '10000')
splitEntry.grid(column=1, row=5)

btn = Button(window, text="Симуляция", command=clicked, width=10, height=1, font=("Arial", 20))
btn.grid(column=0, row=7)

forceText = Label(window, text="Сила = 0", font=("Arial", 20))
forceText.grid(column=0, row=8)


