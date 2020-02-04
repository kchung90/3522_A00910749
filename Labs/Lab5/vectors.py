import math


class Vector:

    def __init__(self, x, y, z):
        self.vector = {"x": x,
                       "y": y,
                       "z": z}

    def __str__(self):
        return f"({self.vector['x']}, {self.vector['y']}, {self.vector['z']})"

    def __getitem__(self, item):
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __add__(self, other):
        result = Vector((self.vector['x'] + other.vector['x']),
                        (self.vector['y'] + other.vector['y']),
                        (self.vector['z'] + other.vector['z']))
        return result

    def __sub__(self, other):
        result = Vector((self.vector['x'] - other.vector['x']),
                        (self.vector['y'] - other.vector['y']),
                        (self.vector['z'] - other.vector['z']))
        return result

    def __mul__(self, other):
        if type(other) == Vector:
            result = Vector(self.vector['y'] * other.vector['z'] -
                            self.vector['z'] * other.vector['y'],
                            self.vector['z'] * other.vector['x'] -
                            self.vector['x'] * other.vector['z'],
                            self.vector['x'] * other.vector['y'] -
                            self.vector['y'] * other.vector['x'])
        else:
            result = Vector(self.vector['x'] * other,
                            self.vector['y'] * other,
                            self.vector['z'] * other)
        return result

    def __rmul__(self, other):
        if type(other) == Vector:
            result = Vector(self.vector['y'] * other.vector['z'] -
                            self.vector['z'] * other.vector['y'],
                            self.vector['z'] * other.vector['x'] -
                            self.vector['x'] * other.vector['z'],
                            self.vector['x'] * other.vector['y'] -
                            self.vector['y'] * other.vector['x'])
        else:
            result = Vector(self.vector['x'] * other,
                            self.vector['y'] * other,
                            self.vector['z'] * other)
        return result

    def __abs__(self):
        magnitude = math.sqrt(self.vector['x'] ** 2 +
                              self.vector['y'] ** 2 +
                              self.vector['z'] ** 2)
        return magnitude

    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        return False

    def __le__(self, other):
        if abs(self) <= abs(other):
            return True
        return False

    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        return False

    def __ge__(self, other):
        if abs(self) >= abs(other):
            return True
        return False

    def __eq__(self, other):
        if abs(self) == abs(other) and \
                self.vector['x'] == other.vector['x'] and \
                self.vector['y'] == other.vector['y'] and \
                self.vector['z'] == other.vector['z']:
            return True
        return False

    def __ne__(self, other):
        if abs(self) != abs(other) and \
                self.vector['x'] != other.vector['x'] and \
                self.vector['y'] != other.vector['y'] and \
                self.vector['z'] != other.vector['z']:
            return True
        return False


def main():
    my_vector = Vector(2, 2, 2)
    # print(my_vector)
    # print(my_vector["x"])
    # my_vector["x"] = 50
    print(my_vector)
    other_vector = Vector(1, 2, 3)
    print(other_vector)

    print(my_vector + other_vector)
    print(my_vector - other_vector)
    print(my_vector * other_vector)
    print(my_vector * 3)
    print(2 * my_vector)


if __name__ == '__main__':
    main()
