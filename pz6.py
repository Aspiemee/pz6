from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--name', help='Название фигуры, например:'
                    'Квадрат, Треугольник, Трапеция, Шестиугольник',
                    type=str)
parser.add_argument('--h', help='Высота выбранной фигуры', type=int)
args = parser.parse_args()

name = args.name
try: 
    height = args.h
    if height < 5: 
        raise ValueError
except ValueError:
    print('Похоже что значение высоты меньше 5')



def triangle(h: int) -> None:
    ...

def square(h: int) -> None:
    ...
    
def trapezoid(h: int) -> None:
    print(6*'*')
    for i in range(1, h):
        print('*' * (6+i))
 
def hexagon(h: int) -> None:
    print('  ' + '*' * 5)
    for i in range(h - 1):
        print('*'*9)
    
match name.lower():
    case 'квадрат':
        triangle(height)
    case 'треугольник':
        square(height)
    case 'трапеция': 
        trapezoid(height)
    case 'шестиугольник':
        hexagon(height)
    case _:
        print('я не знаю такой фигуры(((')