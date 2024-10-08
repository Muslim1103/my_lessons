class House:
    def __init__(self, name, floors):
        """
        Конструктор класса, который инициализирует название дома и количество этажей.
        
        Аргументы:
        name -- название дома (строка)
        floors -- количество этажей (целое число)
        """
        self.name = name      # Название дома
        self.floors = floors  # Количество этажей

    def __str__(self):
        """
        Метод для строкового представления объекта класса.
        Возвращает строку, описывающую название и количество этажей дома.
        """
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    # Методы сравнения

    def __eq__(self, other):
        """
        Перегрузка оператора ==.
        Сравнивает количество этажей у двух объектов класса House.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если количество этажей одинаковое, иначе False.
        """
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __ne__(self, other):
        """
        Перегрузка оператора !=.
        Проверяет неравенство количества этажей у двух объектов класса House.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если количество этажей разное, иначе False.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Перегрузка оператора <.
        Сравнивает, меньше ли количество этажей у текущего дома по сравнению с другим.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если у текущего дома этажей меньше, иначе False.
        """
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        """
        Перегрузка оператора <=.
        Сравнивает, меньше или равно ли количество этажей у текущего дома по сравнению с другим.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если у текущего дома этажей меньше или столько же, иначе False.
        """
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        """
        Перегрузка оператора >.
        Сравнивает, больше ли количество этажей у текущего дома по сравнению с другим.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если у текущего дома этажей больше, иначе False.
        """
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        """
        Перегрузка оператора >=.
        Сравнивает, больше или равно ли количество этажей у текущего дома по сравнению с другим.

        Аргументы:
        other -- другой объект класса House для сравнения
        
        Возвращает True, если у текущего дома этажей больше или столько же, иначе False.
        """
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    # Методы для сложения

    def __add__(self, value):
        """
        Перегрузка оператора +.
        Увеличивает количество этажей на заданное значение.

        Аргументы:
        value -- целое число, на которое нужно увеличить количество этажей
        
        Возвращает новый объект класса House с увеличенным количеством этажей.
        """
        if isinstance(value, int):
            return House(self.name, self.floors + value)
        return NotImplemented  # Если аргумент не число, возвращает NotImplemented

    def __radd__(self, value):
        """
        Перегрузка оператора +, когда число стоит слева (например, 10 + h1).
        Делает то же самое, что и метод __add__.

        Аргументы:
        value -- целое число, на которое нужно увеличить количество этажей
        
        Возвращает результат вызова метода __add__.
        """
        return self.__add__(value)

    def __iadd__(self, value):
        """
        Перегрузка оператора +=.
        Увеличивает количество этажей на заданное значение и изменяет текущий объект.

        Аргументы:
        value -- целое число, на которое нужно увеличить количество этажей
        
        Возвращает текущий объект класса House с увеличенным количеством этажей.
        """
        if isinstance(value, int):
            self.floors += value
        return self

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# Сравнение
print(h1 == h2)  # False

# Увеличиваем этажи с помощью оператора +
h1 = h1 + 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

# Увеличиваем этажи с помощью оператора +=
h1 += 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

# Используем radd (число + объект)
h2 = 10 + h2
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

# Сравнение объектов
print(h1 > h2)   # False
print(h1 >= h2)  # True
print(h1 < h2)   # False
print(h1 <= h2)  # True
print(h1 != h2)  # False
