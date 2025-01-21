import math
import numpy as np
from typing import Union, List, Tuple


class Point:
    def __init__(self, x, y, z=None):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if z is not None and not isinstance(z, (int, float)):
            raise TypeError("z must be a number")
        
        self.x = x
        self.y = y
        if z is not None:
            self.z = z

    def __str__(self):
        if hasattr(self, "z"):
            return f"Point(x={self.x}, y={self.y}, z={self.z})"
        return f"Point(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False

        if hasattr(self, "z") and hasattr(other, "z"):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        if hasattr(self, "z") and hasattr(other, "z"):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        if hasattr(self, "z") and hasattr(other, "z"):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        if hasattr(self, "z"):
            return Point(self.x * other, self.y * other, self.z * other)
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented

        if other == 0:
            return ZeroDivisionError("Cannot divide by zero")

        if hasattr(self, "z"):
            return Point(self.x / other, self.y / other, self.z / other)
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented

        if other == 0:
            return ZeroDivisionError("Cannot divide by zero")

        if hasattr(self, "z"):
            return Point(self.x // other, self.y // other, self.z // other)
        return Point(self.x // other, self.y // other)

    def __mod__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented

        if other == 0:
            return ZeroDivisionError("Cannot divide by zero")

        if hasattr(self, "z"):
            return Point(self.x % other, self.y % other, self.z % other)
        return Point(self.x % other, self.y % other)

    def __pow__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented

        if hasattr(self, "z"):
            return Point(self.x**other, self.y**other, self.z**other)
        return Point(self.x**other, self.y**other)

    def __neg__(self):
        if hasattr(self, "z"):
            return Point(-self.x, -self.y, -self.z)
        return Point(-self.x, -self.y)

    def __abs__(self):
        if hasattr(self, "z"):
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        if hasattr(self, "z") and hasattr(other, "z"):
            return (
                self.x < other.x
                or (self.x == other.x and self.y < other.y)
                or (self.x == other.x and self.y == other.y and self.z < other.z)
            )
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __le__(self, other):
        if hasattr(self, "z") and hasattr(other, "z"):
            return (
                self.x < other.x
                or (self.x == other.x and self.y < other.y)
                or (self.x == other.x and self.y == other.y and self.z <= other.z)
            )
        return self.x < other.x or (self.x == other.x and self.y <= other.y)

    def __gt__(self, other):
        if hasattr(self, "z") and hasattr(other, "z"):
            return (
                self.x > other.x
                or (self.x == other.x and self.y > other.y)
                or (self.x == other.x and self.y == other.y and self.z > other.z)
            )
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def __ge__(self, other):
        if hasattr(self, "z") and hasattr(other, "z"):
            return (
                self.x > other.x
                or (self.x == other.x and self.y > other.y)
                or (self.x == other.x and self.y == other.y and self.z >= other.z)
            )
        return self.x > other.x or (self.x == other.x and self.y >= other.y)

    def __iter__(self):
        yield self.x
        yield self.y
        if hasattr(self, "z"):
            yield self.z

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2 and hasattr(self, "z"):
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2 and hasattr(self, "z"):
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __hash__(self):
        if hasattr(self, "z"):
            return hash((self.x, self.y, self.z))
        return hash((self.x, self.y))

    def copy(self):
        if hasattr(self, "z"):
            return Point(self.x, self.y, self.z)
        return Point(self.x, self.y)

    def distance(self, other: "Point") -> float:
        if not isinstance(other, Point):
            raise TypeError("Other must be a Point object")

        if hasattr(self, "z") and hasattr(other, "z"):
            return math.sqrt(
                (self.x - other.x) ** 2
                + (self.y - other.y) ** 2
                + (self.z - other.z) ** 2
            )
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def rotate(self, angle: float) -> "Point":
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a number")

        if hasattr(self, "z"):
            return Point(
                self.x * math.cos(angle) - self.y * math.sin(angle),
                self.x * math.sin(angle) + self.y * math.cos(angle),
                self.z,
            )
        return Point(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def rotate_yz(self, angle: float) -> "Point":
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a number")

        if not hasattr(self, "z"):
            raise AttributeError("Point must have a z attribute")

        return Point(
            self.x,
            self.y * math.cos(angle) - self.z * math.sin(angle),
            self.y * math.sin(angle) + self.z * math.cos(angle),
        )
        
    def rotate_xz(self, angle: float) -> "Point":
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a number")

        if not hasattr(self, "z"):
            raise AttributeError("Point must have a z attribute")

        return Point(
            self.x * math.cos(angle) - self.z * math.sin(angle),
            self.y,
            self.x * math.sin(angle) + self.z * math.cos(angle),
        )
        
    def rotate_3d(self, angles: List[float]) -> "Point":
        if not isinstance(angles, list):
            raise TypeError("Angles must be a list of 3 numbers")

        if len(angles) != 3:
            raise ValueError("Angles must be a list of 3 numbers")

        if not all(isinstance(angle, (int, float)) for angle in angles):
            raise TypeError("Angles must be a list of 3 numbers")

        if not hasattr(self, "z"):
            raise AttributeError("Point must have a z attribute")

        x, y, z = self.x, self.y, self.z
        rx, ry, rz = angles

        # Rotation matrix for X-axis
        rot_x = np.array([
            [1, 0, 0],
            [0, math.cos(rx), -math.sin(rx)],
            [0, math.sin(rx), math.cos(rx)]
        ])

        # Rotation matrix for Y-axis
        rot_y = np.array([
            [math.cos(ry), 0, math.sin(ry)],
            [0, 1, 0],
            [-math.sin(ry), 0, math.cos(ry)]
        ])

        # Rotation matrix for Z-axis
        rot_z = np.array([
            [math.cos(rz), -math.sin(rz), 0],
            [math.sin(rz), math.cos(rz), 0],
            [0, 0, 1]
        ])

        # Combine rotations
        rotation_matrix = rot_z @ rot_y @ rot_x

        # Apply rotation to the point
        rotated_point = rotation_matrix @ np.array([x, y, z])

        return rotated_point
