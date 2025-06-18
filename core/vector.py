#Create classes called vector2i and 2f to store two values

class vector2i:
    def __init__(self, x: int, y: int) -> "vector2i":
        self.x = x
        self.y = y

    def __add__(self, other: "vector2i") -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other: "vector2i") -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other: "vector2i") -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    def __truediv__(self, other: "vector2i") -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x / other.x, self.y / other.y)
        return NotImplemented
    
    def __repr__(self) -> str:
        return f"{self.x} {self.y}"

class vector2f:
    def __init__(self, x: float, y: float) -> "vector2f":
        self.x = x
        self.y = y

    def __add__(self, other: "vector2f") -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other: "vector2f") -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other: "vector2f") -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    def __truediv__(self, other: "vector2f") -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x / other.x, self.y / other.y)
        return NotImplemented
    
    def __repr__(self) -> str:
        return f"{self.x} {self.y}"