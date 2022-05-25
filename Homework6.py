# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:47:46 2022

@author: dimsa
"""
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в 
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение 
# и завершать скрипт.
import time
from tqdm import tqdm
colors = ['КРАСНЫЙ' , 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']
delays = [7,3,5]
class TrafficLight():
    def __init__(self, __colors, __delays):
       self.__colors = colors
       self.__delays = delays
       
    def timer(sec):
        while sec != 0:
            print(sec,'(...)')
            time.sleep(1)
            sec -= 1    
            
    def running(self):    
        for i in tqdm(range(3)):
            print(f'\nЦвет светофора: {colors[i]}')
            TrafficLight.timer(delays[i])
    
a = TrafficLight(colors, delays)
a.running()

# Цветной светофор #для себя
import time
from tqdm import tqdm
delays = [7, 3, 5]
colors = ['КРАСНЫЙ' , 'ЖЕЛТЫЙ', 'ЗЕЛЕНЫЙ']
class TrafficLight():
    def __init__(self, colors, delays):
       self.__colors = colors
       self.__delays = delays
    def timer(sec):
        while sec != 0:
            print(sec,'(...)')
            time.sleep(1)
            sec -= 1    
    
    def running(self):    
        for i in (range(3)):
            if i == 0:
                print("\033[7m\033[37m\033[41m{}\033[0m".format(f'\nЦвет светофора: {colors[0]}'))
                TrafficLight.timer(delays[0])
            elif i == 1:
                print("\033[7m\033[37m\033[43m{}\033[0m".format(f'\nЦвет светофора: {colors[1]}'))
                TrafficLight.timer(delays[1])
            elif i == 2:
                print("\033[7m\033[37m\033[42m{}\033[0m".format(f'\nЦвет светофора: {colors[2]}'))
                TrafficLight.timer(delays[2])
            else:
                pass
            
a = TrafficLight(colors, delays)
a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
# Значения данных атрибутов должны передаваться при создании экземпляра класса. 
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def calc_road():
        p = int(input('Введите плотнось асфальта, кг/m2 для 1 см толщины:'))
        d = int(input('Длина дороги, км:'))
        s = int(input('Ширина дороги, м:'))
        t = int(input('Тольщина полотна, см:'))
        AllRoad = p * t * d * s
        print('Масса асфальта:', AllRoad, 'т.')
        print(f'Вам необходимо: {AllRoad // 20} полных фур')
        
a = Road
a.calc_road()
        
        
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника 
#(get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса
#Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.        
    
class Worker:
    
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
       
class Position(Worker):
   
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
       
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker_name = input('Введите имя: ')
worker_surname = input('Введите фамилию: ')
worker_position = input('Введите должность: ')
worker_wage = int(input('Введите зарплату: '))
worker_bonus = int(input('Введите премию: '))
a = {}
a['wage'], a['bonus'] = worker_wage, worker_bonus
#print(a)
pos = Position(worker_name, worker_surname, worker_position, a)
print(f'Full name is: {pos.get_full_name()}')
print(f'Position of the worker is: {pos.position}')
print(f'Total income is: {pos.get_total_income()}')

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = is_police
    
    def car_go(self):
        print(f'{self.__color} {self.__name} поехала')
    
    def car_stop(self):
        print(f'{self.__color} {self.__name} остановилась')
    
    def car_turn(self, side):
       print(f'{self.__color} {self.__name} повернула на{side}')
       
    def show_speed(self):
        print(f'текущая скорость: {self._speed} км/ч')
        
    def police(self):
        return self.__is_police
        
      
class TownCar(Car):
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, 'Нет!')
        
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f'Превышение скорости на {self._speed - 60} км/ч!')
        
class SportCar(Car):
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, 'Нет!')        
            
class WorkCar(Car):
    
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, 'Нет!') 
        
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f'Превышение скорости на {self._speed - 40} км/ч!')

class PoliceCar(Car):
    
    def __init__(self, speed, color, namee):
        super().__init__(speed, color, name, 'Да!')  

def car_movings(exact):
    exact.car_go()
    exact.car_turn("право")
    exact.car_turn("лево")
    exact.show_speed()
    print("Полицеская машина?: ", exact.police())
    exact.car_stop()              
    
speed = 80
color = 'Красная'
name = 'рабочая Машина'
work = WorkCar(speed, color, name)
car_movings(work)       

speed = 65
color = 'Желтая'
name = 'городская машина'
town = TownCar(speed, color, name)
car_movings(town)

speed = 120
color = 'Специальная'
name = 'полицейская машина'
police = PoliceCar(speed, color, name)
car_movings(police)

speed = 150
color = 'Синяя'
name = 'спортивная машина'
sport = SportCar(speed, color, name)
car_movings(sport)

# 5. Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” 
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. 
# Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    
    def __init__(self, title):
        self._title = title
        
    def draw(self):
        print(f'{self._title}: Старт отрисовки в родительском классе')

class Pen(Stationery):
    
    def draw(self):
        print(f'{self._title}: Старт отрисовки в дочернем классе *РУЧКА*')
    
class Pencil(Stationery):
    
    def draw(self):
        print(f'{self._title}: Старт отрисовки в дочернем классе *КАРАНДАШ*')
    
class Handle(Stationery):
    
    def draw(self):
        print(f'{self._title}: Старт отрисовки в дочернем классе *МАРКЕР*')



rod = Stationery('Родительский класс')
rod.draw()
ruch = Pen('Класс РУЧКА')
ruch.draw()
kar = Pencil('Класс КАРАНДАШ')
kar.draw()
mar = Handle('Класс МАРКЕР')
mar.draw()
        
    
        
        
        