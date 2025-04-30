import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotate(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        new_x = self.x * math.cos(angle_radians) - self.y * math.sin(angle_radians)
        new_y = self.x * math.sin(angle_radians) + self.y * math.cos(angle_radians)
        return Vector2D(new_x, new_y)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

# User Input
dimension = input("Enter vector dimension (2D/3D): ").lower()

if dimension == "2d":
    x = float(input("Enter x component of vector: "))
    y = float(input("Enter y component of vector: "))
    v1 = Vector2D(x, y)
    print("Magnitude of the vector:", v1.magnitude())
elif dimension == "3d":
    x = float(input("Enter x component of vector: "))
    y = float(input("Enter y component of vector: "))
    z = float(input("Enter z component of vector: "))
    v1 = Vector3D(x, y, z)
    print("Magnitude of the vector:", v1.magnitude())
