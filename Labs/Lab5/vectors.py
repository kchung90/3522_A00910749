class Vector:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        pass

    def __getitem__(self, item):
        if item == "x":
            return self._x
        elif item == "y":
            return self._y
        elif item == "z":
            return self._z


def main():
    dir()


if __name__ == '__main__':
    main()