# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
from math import pi

class Circle:
    def __init__(self, radius, fill ='red', stroke='black'):
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



def main():
    circle = Circle(5.0, fill='orange', stroke='red')
    print(f"area = {circle.calculate_area()}")

    circle2 = Circle(8.0)
    return 0 # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
