# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
from math import pi
import yaml

class Circle:
    def __init__(self, radius, fill ='red', stroke='black', at=(0,0)):
        self._at = at
        self._radius = radius
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        return pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    def __len__(self):
        return 2 * pi * self._radius

    def __string__(self):
        string = {
            'circle': {
                'radius': self._radius,
                'at': self._at,
                'stroke': self._stroke,
                'fill': self._fill
            }
        }
        return string

    @classmethod
    def from_yaml(cls, string):
        '''create a circle from a YAML string'''
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill = circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj

class Quad:
    def __init__(self, width, height, fill ='green', stroke='pink'):
        self._height = height
        self._width = width
        self._fill = fill
        self._stroke = stroke

    def area(self):
        return float(self.width * self._height)

class Canvas:
    def __init__(self, height, width, bg = 'orange'):
        self._height = height
        self._width = width
        self._bg = bg

class Text:
    def __init__(self, text, font, size, color):
        self._text = text
        self._font = font
        self._size = size
        self._color = color



def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")

    circle2 = Circle(8.0)

    my_dict = {
        'key': {
            'inside_dict': [5,6,7,8]
        }
    }
    my_yaml = yaml.dump(circle.__string__())
    print(my_yaml)

    yaml_circle = '''\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red
    '''
    my_circle = Circle.from_yaml(yaml_circle)
    return 0 # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/