class Line:
    def __init__(self, x1, y1, x2, y2):
        # start and end points
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)

        # slope and y-intercept (assume slope not infinity)
        self.slope = (y2 - y1) / (x2 - x1)
        self.y_intercept = y1 - self.slope * x1

    def contains(self, x, y):
        """Return True if (x,y) lies on the line segment"""
        # check if (x, y) satisfies line equation
        if abs(y - (self.slope * x + self.y_intercept)) > 1e-6:
            return False

        # check if (x,y) lies between start_point and end_point
        min_x, max_x = min(self.start_point.get_x(), self.end_point.get_x()), max(self.start_point.get_x(), self.end_point.get_x())
        min_y, max_y = min(self.start_point.get_y(), self.end_point.get_y()), max(self.start_point.get_y(), self.end_point.get_y())

        return min_x <= x <= max_x and min_y <= y <= max_y

    def get_distance(self):
        """Return distance between start_point and end_point"""
        return ((self.end_point.get_x() - self.start_point.get_x()) ** 2 + 
                         (self.end_point.get_y() - self.start_point.get_y()) ** 2) ** 0.5

    def get_x1(self):
        return self.start_point.get_x()

    def get_y1(self):
        return self.start_point.get_y()

    def get_x2(self):
        return self.end_point.get_x()

    def get_y2(self):
        return self.end_point.get_y()

    def get_y(self, x):
        """Return y for given x if it lies between start_point and end_point, else -999.999"""
        y = self.slope * x + self.y_intercept

        min_x, max_x = min(self.start_point.get_x(), self.end_point.get_x()), max(self.start_point.get_x(), self.end_point.get_x())
        min_y, max_y = min(self.start_point.get_y(), self.end_point.get_y()), max(self.start_point.get_y(), self.end_point.get_y())

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return y
        else:
            return -999.999

class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0: return True
        else: return False

    def is_on_y_axis(self):
        if self.__x == 0: return True
        else: return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
  
n = Line(1, 1, 4, 4)

print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
print(n.contains(0.0, 0.0))
print(n.contains(1.0, 1.0))
print(n.contains(1.0, 0.0))
print(n.contains(0.0, 1.0))
print(n.contains(2.0, 0.0))
print(n.contains(0.0, 3.0))
print(n.get_distance())
print(n.get_y(3))
print(n.get_y(0))