import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(a, b):
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Example usage:
point_a = Point(1, 2)
point_b = Point(4, 6)
distance = distance_between_points(point_a, point_b)
print(distance)  # This will print the distance between point_a and point_b