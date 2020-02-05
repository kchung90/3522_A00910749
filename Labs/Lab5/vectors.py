"""
@author Kevin Chung

This module overloads the mathematical operators to perform addition,
subtraction, and multiplication of two vectors, and compare their
magnitude and direction.
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
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Return the description of the Vector object
        :return: the description as a String
        """
        return f"({self.x}, {self.y}, {self.z})"

    def __getitem__(self, item):
        """
        Get the attribute of the Vector object
        :param item: coordinate to get as a String
        :return: coordinate value as a float
        """
        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        elif item == "z":
            return self.z

    def __setitem__(self, key, value):
        """
        Set the attribute of the Vector object
        :param key: coordinate to be set as a String
        :param value: value of the coordinate as a float
        """
        if key == "x":
            self.x = value
        elif key == "y":
            self.y = value
        elif key == "z":
            self.z = value

    def __add__(self, other):
        """
        Add two vectors together
        :param other: a Vector object to be added
        :return: a Vector object
        """
        return Vector((self.x + other.x), (self.y + other.y),
                      (self.z + other.z))

    def __sub__(self, other):
        """
        Subtract another vector from a vector
        :param other: a Vector object to be subtracted
        :return: a Vector object
        """
        return Vector((self.x - other.x), (self.y - other.y),
                      (self.z - other.z))

    def __mul__(self, other):
        """
        Multiply a vector with another vector or a scalar
        :param other: a Vector object or a float to be multiplied
        :return: a Vector object
        """
        if type(other) == Vector:
            return Vector(self.y * other.z - self.z * other.y,
                          self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        """
        Reflection multiplication of a vector with another vector or a
        scalar. This method was added to ensure that the multiplication
        works even when the order is
        flipped.
        :param other: a Vector object or a float to be multiplied
        :return: a Vector object
        """
        if type(other) == Vector:
            result = Vector(self.y * other.z - self.z * other.y,
                            self.z * other.x - self.x * other.z,
                            self.x * other.y - self.y * other.x)
        else:
            result = Vector(self.x * other, self.y * other, self.z * other)
        return result

    def __abs__(self):
        """
        Calculate the magnitude of the vector
        :return: magnitude of the vector as a float
        """
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return magnitude

    def __lt__(self, other):
        """
        Compare two vectors to find out if a vector is less than the
        other vector
        :param other: a Vector object to be compared
        :return: result as a Bool
        """
        if abs(self) < abs(other):
            return True
        return False

    def __le__(self, other):
        """
        Compare two vectors to find out if a vector is less than or
        equal to the other vector
        :param other: a Vector object to be compared
        :return: result as a Bool
        """
        if abs(self) <= abs(other) and self.x == other.x and \
                self.y == other.y and self.z == other.z:
            return True
        return False

    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        return False

    def __ge__(self, other):
        if abs(self) >= abs(other) and self.x == other.x and \
                self.y == other.y and self.z == other.z:
            return True
        return False

    def __eq__(self, other):
        if abs(self) == abs(other) and self.x == other.x and \
                self.y == other.y and self.z == other.z:
            return True
        return False

    def __ne__(self, other):
        if abs(self) != abs(other) and self.x != other.x and \
                self.y != other.y and self.z != other.z:
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
