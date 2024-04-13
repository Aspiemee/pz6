from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--name', help='Название фигуры, например:'
                    'Квадрат, Треугольник, Трапеция, Шестиугольник',
                    type=str)
parser.add_argument('--h', help='Высота выбранной фигуры(минимальное значение равно 5)', type=int)
args = parser.parse_args()


#проверка ввода данных
try: 
    if not args.name or not args.h:
        raise Exception
    name = args.name
    height = args.h
    if height < 5: 
        raise ValueError
except ValueError:
    print('Похоже что значение высоты меньше 5')
    exit()
except Exception:
    print('Вы не ввели какие то данные')
    exit()

#функции для вывода фигур в консоль
def triangle(h: int) -> None:
    for i in range(1, h + 1):
        print(" " * (h - i) + "*" * (2 * i - 1))

def square(h: int) -> None:
    for i in range(1, h + 1):
        print("*  " * h)
    
def trapezoid(h: int) -> None:
    print(6*'*')
    for i in range(1, h):
        print('*' * (6+i))
 
def hexagon(h: int) -> None:
    print('  ' + '*' * 5)
    for i in range(h - 1):
        print('*'*9)
    
#блок для проверки ввода названия фигуры и вызова нужной функции 
match name.lower():
    case 'квадрат':
        square(height)
    case 'треугольник':
        triangle(height)
    case 'трапеция':
        trapezoid(height)
    case 'шестиугольник':
        hexagon(height)
    case _:
        print('я не знаю такой фигуры(((')