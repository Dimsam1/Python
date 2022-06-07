
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — 
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import random as rnd

class Matrix:
    def __init__(self, matr1, matr2):
        self.matr1 = matr1
        self.matr2 = matr2

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))

    def __add__(self):
        self.matr = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for x in range(len(self.matr1)):
            for y in range(len(self.matr2[x])):
                self.matr[x][y] = self. matr1[x][y] + self.matr2[x][y]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matr]))
     
Rows = 3
Cols = 3
matrix1 = [([rnd.randint(0, 100) for i in range(Cols)]) for x in range(Rows)]
print(f' Первая матрица: {matrix1}')
matrix2 = [[rnd.randint(0, 100) for i in range(Cols)] for x in range(Rows)]
print(f' Вторая матрица: {matrix2}')
res_matrix = Matrix(matrix1, matrix2)
print(res_matrix.__add__())

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes():
    def get_tissue_consumption(self):
        pass

    @property
    def tissue_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def get_tissue_consumption(self):
        return 2 * self.__height + 0.3

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def get_tissue_consumption(self):
        return self.__size/6.5 + 0.5

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


size = int(input("Input int size for a coat: "))
coat = Coat(size)
print(f'Tissue consumption for the coat in size {coat.size}: {coat.tissue_consumption}')

height = float(input("Input height for a suit: "))
suit = Suit(height)
print(f'Tissue consumption for the suit with height {suit.height}: {suit.tissue_consumption}')


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
# умножение и обычное (не целочисленное) деление клеток, соответственно. 
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
#  иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Разница отрицательна!')

    def __mul__(self, other):

        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):

        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(10)
cells2 = Cell(50)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(3))
print(cells1 / cells2) 



