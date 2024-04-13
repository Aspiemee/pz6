from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--name', help='Название фигуры, например:'
                    'Квадрат, Треугольник, Трапеция, Шестиугольник',
                    type=str)
parser.add_argument('--h', help='Высота выбранной фигуры', type=int)
args = parser.parse_args()

name = args.name
height = args.h


def triangle(h: int) -> None:
    ...

def square(h: int) -> None:
    ...
    
def trapezoid(h: int) -> None:
    if h < 5:
        print('Высота шестиугольника не может быть меньше 5!')
    else:
        print(6*'*')
        for i in range(1, h):
            print('*' * (6+i))
 
def hexagon(h: int) -> None:
    if h < 5:
        print('Высота шестиугольника не может быть меньше 5!')
    else:
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