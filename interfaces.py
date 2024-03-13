import argparse

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Circle:
    def __init__(self, center: Point, radius):
        if isinstance(center, Point):
            self.center = center
        else:
            raise TypeError('Got non-Point argument')
        self.radius = radius

def read_objects_from_file(filename):
    valid_objects = []
    valid_lines = []
    invalid_lines = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    obj = eval(line.strip())
                    if isinstance(obj, (Point, Line, Circle)):
                        valid_objects.append(obj)
                        valid_lines.append(line)
                    else:
                        invalid_lines.append(f"Неверный формат данных в строке {line_number}: {line.strip()}")
                except Exception as e:
                    invalid_lines.append(f"Ошибка в строке {line_number}: {e}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    for line in invalid_lines:
        print(line)
    return valid_lines, invalid_lines

def main():
    parser = argparse.ArgumentParser(description="Обработка данных из файла")
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-o', '--oper', type=str, required=True, choices=['print', 'count'])
    args = parser.parse_args()

    if args.oper == 'print':
        valid_lines, _ = read_objects_from_file(args.file)
        for line in valid_lines:
            print(line, end='')
    elif args.oper == 'count':
        objects, _ = read_objects_from_file(args.file)
        print(f"Количество объектов: {len(objects)}")

if __name__ == "__main__":
    main()