class Vector:

    def __init__(self, x, y, z):
        self.vector = {"x": x,
                       "y": y,
                       "z": z}

    def __str__(self):
        return f"{self.vector['x']}, {self.vector['y']}, {self.vector['z']}"

    def __getitem__(self, item):
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value


def main():
    my_vector = Vector(10, 20, 30)
    print(my_vector)
    print(my_vector["x"])
    my_vector["x"] = 50
    print(my_vector)


if __name__ == '__main__':
    main()
