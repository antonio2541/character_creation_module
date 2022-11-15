from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень из введённого вами числа."""
    otvet = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа. '
          'Это будет: ' + str(otvet))


print(message)
calc(25.5)
