# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
# с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date():
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def number(cls, check_date):
        day, month, year = map(int, check_date.split("-"))
        print(f'День: {day}, месяц: {month}, год:{year}')

    @staticmethod
    def valid(check_date):
        day, month, year = map(int, check_date.split("-"))
        if day > 31:
            print('Значение дня не должно  быть положительным и не превышать 31')
        if month > 12:
            print('Значение месяца не должно превышать 12')
        if year > 2022:
            print('Значение года не должно превышать 2022')


date_inp = Date.number(x := input('Введите дату в формате дд-мм-гггг ')) 
# вот и пригодился оператор моржа := (версия от 3.9), прикольно...))
date_check = Date.valid(x)


# Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class devis():
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def func(self):
        try:
            return(f'Результат деления: {round((self.num1/self.num2), 2)}')
        except ZeroDivisionError:
            return "На 0 делить нельзя!"


a = devis(5,0)
print(a.func())
b = devis(8,3)
print(b.func())

 
#3 Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
class err():
    def inp(self):
        new_d= []
        while(True):
            st = str(input("Введите значение: "))
            if st !='':
                for i in st:
                    if i.isdigit():
                        new_d.append(i)
            else:
                break
        print(new_d)

a = err()
a.inp()

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class sklad():
    def __init__(self):
        self.arr = []

class tech():
    def __init__(self, price, color, weight):
        self.price = price
        self. color = color
        self.weight = weight

class printer(tech):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed


class scanner(tech):
    def __init__(self, price, color, weight, lamp):
        super().__init__(price, color, weight)
        self.lamp = lamp

class xerox(tech):
    def __init__(self, price, color, weight, pages):
        super().__init__(price, color, weight)
        self.pages = pages

prin = printer(100, "white", 3.2, 16)
scan = scanner(200, 'black', 2.5, 50)


# 5. Продолжить работу над первым заданием. 
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).

class sklad():
    def __init__(self):
        self.arr = {"printer": 3, "scanner": 0, "xerox": 0}

    def priem(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.arr["printer"] = int(self.arr.get("printer")) + self.quantity
        if self.name == 'scanner':
            self.arr["scanner"] = int(self.arr.get("scanner")) + self.quantity
        if self.name == 'xerox':
            self.arr["xerox"] = int(self.arr.get("xerox")) + self.quantity
        print(f'Был добавлен {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')

    def spisanie(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.arr["printer"] = int(self.arr.get("printer")) - self.quantity
        if self.name == 'scanner':
            self.arr["scanner"] = int(self.arr.get("scanner")) - self.quantity
        if self.name == 'xerox':
            self.arr["xerox"] = int(self.arr.get("xerox")) - self.quantity
        print(f'Был списан {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')

class tech():
    def __init__(self, price, color, weight):
        self.price = price
        self. color = color
        self.weight = weight

class printer(tech):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed


class scaner(tech):
    def __init__(self, price, color, weight, lamp):
        super().__init__(price, color, weight)
        self.lamp = lamp

class xerox(tech):
    def __init__(self, price, color, weight, pages):
        super().__init__(price, color, weight)
        self.pages = pages

prin = printer(100, "white", 3.2, 16)
scan = scanner(200, 'black', 2.5, 50)

a = sklad()
a.priem("printer", 5)
a.spisanie("printer", 3)
a.priem("xerox", 4)



# 6. Продолжить работу над вторым заданием. 
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
class sklad():
    def __init__(self):
        self.arr = {"printer": 0, "scanner": 0, "xerox": 0}

    def priem(self, name, quantity):
        self.quantity = quantity
        self.name = name
        try:
            if self.name == 'printer':
                self.arr["printer"] = int(self.arr.get("printer")) + self.quantity
            if self.name == 'scanner':
                self.arr["scanner"] = int(self.arr.get("scanner")) + self.quantity
            if self.name == 'xerox':
                self.arr["xerox"] = int(self.arr.get("xerox")) + self.quantity
            print(f'Был добавлен {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")

    def spisanie(self, name, quantity):
        self.quantity = quantity
        self.name = name

        try:
            if self.name == 'printer':
                self.arr["printer"] = int(self.arr.get("printer")) - quantity
            if self.name == 'scanner':
                self.arr["scanner"] = int(self.arr.get("scanner")) - quantity
            if self.name == 'xerox':
                self.arr["xerox"] = int(self.arr.get("xerox")) - quantity
            print(f'Был списан {self.name}  в количестве {quantity} шт. Актуальное состояние склада {self.arr}')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")


class tech():
    def __init__(self, price, color, weight):
        self.price = price
        self. color = color
        self.weight = weight

class printer(tech):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed


class scaner(tech):
    def __init__(self, price, color, weight, lamp):
        super().__init__(price, color, weight)
        self.lamp = lamp

class xerox(tech):
    def __init__(self, price, color, weight, pages):
        super().__init__(price, color, weight)
        self.pages = pages

prin = printer(100, "white", 3.2, 16)
a = sklad()
a.priem("printer", 8)
a.priem("scanner", 6)

a.spisanie("printer", 4)

# 7.Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, cel, mnim):
        self.cel = cel
        self.mnim = mnim

    def __add__(self, other):
        print(f'Сумма n1 и n2 равна')
        return f'z = {self.cel + other.cel} + {self.mnim + other.mnim}j'

    def __mul__(self, other):
        print(f'Произведение n1 и n2 равно')
        return f'z = {(self.cel * other.cel - self.mnim * other.mnim)} + {self.cel * other.mnim + other.cel * self.mnim}j'

    def __str__(self):
        return f'z = {self.cel} + {self.mnim}j'

n1 = ComplexNumber(3, 5)
n2 = ComplexNumber(5, 3)
print('Комплексное число1: ', n1)
print('Комплексное число2: ', n2)
print(n1 + n2)
print(n1 * n2)

#print(type(5+4j))