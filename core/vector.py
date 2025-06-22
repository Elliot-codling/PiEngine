# Create classes called vector2i and 2f to store two values
from typing import Union

# === Vector int ===
class vector2i:
    # === Create vector2i ===
    def __init__(self, x: int, y: int) -> "vector2i":
        self.x = x
        self.y = y

    # Add two vectors, it can be float or int.
    # Returns an int
    def __add__(self, other: Union["vector2i", "vector2f"]) -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x + other.x, self.y + other.y)
        if isinstance(other, vector2f):
            return vector2i(self.x + other.x, self.y + other.y)
        
        return NotImplemented
    
    # Subtract two vectors, it can be float or int.
    # Returns an int
    def __sub__(self, other: Union["vector2i", "vector2f"]) -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x - other.x, self.y - other.y)
        if isinstance(other, vector2f):
            return vector2i(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    # Multiply two vectors, it can be float or int.
    # Returns an int
    def __mul__(self, other: Union["vector2i", "vector2f"]) -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x * other.x, self.y * other.y)
        if isinstance(other, vector2f):
            return vector2i(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    # Divide two vectors, it can be float or int.
    # Returns an int
    def __truediv__(self, other: Union["vector2i", "vector2f"]) -> "vector2i":
        if isinstance(other, vector2i):
            return vector2i(self.x / other.x, self.y / other.y)
        if isinstance(other, vector2f):
            return vector2i(self.x / other.x, self.y / other.y)
        return NotImplemented
    
    # Print the vector
    def __repr__(self) -> str:
        return f"{self.x} {self.y}"

# === Vector float ===
class vector2f:
    # === Create vector2f ===
    def __init__(self, x: float, y: float) -> "vector2f":
        self.x = x
        self.y = y

    # Add two vectors, it can be float or int.
    # Returns an float
    def __add__(self, other: Union["vector2i", "vector2f"]) -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x + other.x, self.y + other.y)
        if isinstance(other, vector2i):
            return vector2f(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    # Subtract two vectors, it can be float or int.
    # Returns an float
    def __sub__(self, other: Union["vector2i", "vector2f"]) -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x - other.x, self.y - other.y)
        if isinstance(other, vector2i):
            return vector2f(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    # Multiply two vectors, it can be float or int.
    # Returns an float
    def __mul__(self, other: Union["vector2i", "vector2f"]) -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x * other.x, self.y * other.y)
        if isinstance(other, vector2i):
            return vector2f(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    # Divide two vectors, it can be float or int.
    # Returns an float
    def __truediv__(self, other: Union["vector2i", "vector2f"]) -> "vector2f":
        if isinstance(other, vector2f):
            return vector2f(self.x / other.x, self.y / other.y)
        if isinstance(other, vector2i):
            return vector2f(self.x / other.x, self.y / other.y)
        return NotImplemented
    
    # Print the vector
    def __repr__(self) -> str:
        return f"{self.x} {self.y}"