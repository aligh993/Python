# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

class Foo:

    def __init__(self):
        self.x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value > 0:
            value %= 100
        elif value < 0:
            value = -1
        self._x = value
