"""
@author Kevin Chung

This module overloads the arithmetic operators and comparison operators
to perform addition, subtractions, and multiplication of two vectors,
and compare their values.
"""
import math


class Vector:
    """
    Represents a vector object which has values for x-coordinate,
    y-coordinate, and z-coordinate
    """
    def __init__(self, x, y, z):
        """
        Initialize a vector object by taking in values for its
        x-coordinate, y-coordinate, and z-coordinate
        :param x: x-coordinate value as a float
        :param y: y-coordinate value as a float
        :param z: z-coordinate value as a float
        """
        self.vector = {"x": x,
                       "y": y,
                       "z": z}

    def __str__(self):
        """
        Return the description of the vector object
        :return: the description as a String
        """
        return f"({self.vector['x']}, {self.vector['y']}, {self.vector['z']})"

    def __getitem__(self, item):
        """
        Get the attribute of the vector object
        :param item: key of the dictionary
        :return: value of the dictionary
        """
        return self.vector[item]

    def __setitem__(self, key, value):
        """
        Set the attribute of the vector object
        :param key: key of the dictionary as a String
        :param value: value of the dictionary as a float
        :return: value of the dictionary at index key as a float
        """
        self.vector[key] = value

    def __add__(self, other):
        """
        Add two vectors together
        :param other: a Vector object to be added
        :return: a Vector object
        """
        result = Vector((self.vector['x'] + other.vector['x']),
                        (self.vector['y'] + other.vector['y']),
                        (self.vector['z'] + other.vector['z']))
        return result

    def __sub__(self, other):
        """
        Subtract two vectors together
        :param other: a Vector object to be subtracted
        :return: a Vector object
        """
        result = Vector((self.vector['x'] - other.vector['x']),
                        (self.vector['y'] - other.vector['y']),
                        (self.vector['z'] - other.vector['z']))
        return result

    def __mul__(self, other):
        """
        Multiply two objects together
        :param other: a Vector object or a float to be multiplied
        :return: a Vector object
        """
        if type(other) == Vector:
            result = Vector(other.vector['z'] * self.vector['y'] -
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
        """
        Multiplication reflection of two objects. This method was added
        to ensure that the multiplication works even when the order is
        flipped.
        :param other: a Vector object or a float to be multiplied
        :return: a Vector object
        """
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
        """
        Calculate the magnitude of the vector object
        :return: magnitude of the vector object as a float
        """
        magnitude = math.sqrt(self.vector['x'] ** 2 +
                              self.vector['y'] ** 2 +
                              self.vector['z'] ** 2)
        return magnitude

    def __lt__(self, other):
        """
        Compare two vectors to find out if the vector is less than the
        other vector
        :param other: a Vector object to be compared
        :return: result as a Bool
        """
        if abs(self) < abs(other):
            return True
        return False

    def __le__(self, other):
        """
        Compare two vectors to find out if the vector is less than or
        eqaul to the other vector
        :param other: a Vector obejct to be compared
        :return: result as a Bool
        """
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
    my_vector = Vector(1, 3, 7)
    other_vector = Vector(2, 4, 6)

    print(f"First vector: {my_vector}")
    print(f"Second vector: {other_vector}")
    print(f"x-coordinate of the first vector: {my_vector['x']}")
    my_vector['x'] = 5
    print(f"Update x-coordinate of the first vector to 5: {my_vector}")

    print(f"\nAdd 2 vectors: {my_vector + other_vector}")
    print(f"Subtract second vector from first vector: "
          f"{my_vector - other_vector}")
    print(f"Multiply 2 vectors: {my_vector * other_vector}")
    print(f"Multiply the first vector with 3: {my_vector * 3}")
    print(f"Multiply the second vector with 2: {2 * other_vector}")
    print(f"Magnitude of the first vector: {abs(my_vector)}")
    print(f"Magnitude of the second vector: {abs(other_vector)}")

    print(f"\nIs the first vector less than the second vector? "
          f"{my_vector < other_vector}")
    print(f"Is the first vector less than or equal to the second vector? "
          f"{my_vector <= other_vector}")
    print(f"Is the first vector greater than the second vector? "
          f"{my_vector > other_vector}")
    print(f"Is the first vector greater than or equal to the second vector? "
          f"{my_vector >= other_vector}")
    print(f"Is the first vector equal to the second vector? "
          f"{my_vector == other_vector}")
    print(f"Is the first vector not equal to the second vector? "
          f"{my_vector != other_vector}")


if __name__ == '__main__':
    main()
