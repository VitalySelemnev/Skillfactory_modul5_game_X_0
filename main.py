# ИГРА КРЕСТИКИ НОЛИКИ


def pole_x_0(matrix):
    print("   ", "0", " ", "1", " ", "2")
    print("---", "-", " ", "-", " ", "---")
    print("0 |", matrix[0][0], "|", matrix[0][1], "|", matrix[0][2], "|")
    print("1 |", matrix[1][0], "|", matrix[1][1], "|", matrix[1][2], "|")
    print("2 |", matrix[2][0], "|", matrix[2][1], "|", matrix[2][2], "|")

def input_player1():
    print("Игрок №1 поставте крестик на поле, для чего укажите координаты на поле [№строки] и [№столбца]")
    global i, j
    i = int(input("Введите [№строки] : "))
    j = int(input("Введите [№столбца]: "))
    while i not in [0, 1, 2] or j not in [0, 1, 2]:
        print("Координаты введены не верно, введите еще раз")
        i = int(input("Введите [№строки] : "))
        j = int(input("Введите [№столбца]: "))
    while matrix[i][j] == "X" or matrix[i][j] == "0":
        print("Введите другие координаты, данная клетка занята")
        i = int(input("Введите [№строки] : "))
        j = int(input("Введите [№столбца]: "))



def input_player2():
    global i, j
    print("Игрок №2 поставте нолик на поле, для чего укажите координаты на поле [№строки] и [№столбца]")
    i = int(input("Введите [№строки] : "))
    j = int(input("Введите [№столбца]: "))
    while i not in [0, 1, 2] or j not in [0, 1, 2]:
        print("Координаты введены не верно, введите еще раз")
        i = int(input("Введите [№строки] : "))
        j = int(input("Введите [№столбца]: "))
    while matrix[i][j] == "X" or matrix[i][j] == "0":
        print("Введите другие координаты, данная клетка занята")
        i = int(input("Введите [№строки] : "))
        j = int(input("Введите [№столбца]: "))



rows = 3
cols = 3
elements = rows * cols


matrix = [
    [" ", " ", " "]
    ,[" ", " ", " "]
    ,[" ", " ", " "]
]

pole_x_0(matrix)
for n in range(elements):
    if (matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0] and matrix[0][0] == "X" or
        matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1] and matrix[0][1] == "X" or
        matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2] and matrix[0][2] == "X" or
        matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2] and matrix[0][0] == "X" or
        matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2] and matrix[1][0] == "X" or
        matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2] and matrix[2][0] == "X" or
        matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] and matrix[0][0] == "X" or
        matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2] and matrix[2][0] == "X"):
        print("Игра окончена, победил Х")
        break

    elif (matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0] and matrix[0][0] == "0" or
        matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1] and matrix[0][1] == "0" or
        matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2] and matrix[0][2] == "0" or
        matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2] and matrix[0][0] == "0" or
        matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2] and matrix[1][0] == "0" or
        matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2] and matrix[2][0] == "0" or
        matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] and matrix[0][0] == "0" or
        matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2] and matrix[2][0] == "0"):
        print("Игра окончена, победил 0")
        break


    if n % 2 == 0:
        input_player1()
        print(matrix[i][j])
        matrix[i][j] = 'X'
        pole_x_0(matrix)
        if n == 8: print("Игра окончена, НИЧЬЯ")
    else:
        input_player2()
        print(matrix[i][j])
        matrix[i][j] = '0'
        pole_x_0(matrix)


