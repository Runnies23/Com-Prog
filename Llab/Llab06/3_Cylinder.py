import math


class Cylinder:
    """Constructor and setting Class Variable"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    """get_radius()"""
    def get_radius(self):
        return self.radius

    """get_height()"""
    def get_height(self):
        return self.height

    """set_radius()"""
    def set_radius(self, radius):
        self.radius = radius

    """set_height()"""
    def set_height(self, height):
        self.height = height

    """get_base_area()"""
    def get_base_area(self):
        return math.pi * self.radius * self.radius

    """get_volume()"""
    def get_volume(self):
        return self.get_base_area() * self.height



    """__str__()"""
    def __str__(self):
        return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"
    

print(Cylinder(7,10))
print(Cylinder(7,10).get_volume())
print(Cylinder(7,10).get_base_area())
    