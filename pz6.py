from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--name', help='Название фигуры, например:'
                    'Квадрат, Треугольник, Трапеция, Шестиугольник',
                    type=str)
parser.add_argument('--h', help='Высота выбранной фигуры', type=int)
args = parser.parse_args()

name = args.name
height = args.height

def triangle(h: int) -> None:
    ...

def square(h: int) -> None:
    ...
    
def trapezoid(h: int) -> None:
    ...

def hexagon(h: int) -> None:
    ...
    
match name.lower():
    case 'квадрат':
        triangle(height)
    case 'треугольник':
        square(height)
    case 'трапеция': 
        trapezoid(height)
    case 'шестиугольник':
        hexagon(height)