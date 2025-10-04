# === External libs ===
# === Inherited classes ===
# === Internal classes ===
from ..vector.Vector import *

# === Transform text ===
class Transform:
    def setPosition(self, position: vector2f) -> None:
        self.m_position = position

    def incrementPosition(self, position: vector2f) -> None:
        self.m_position += position

    def getPosition(self) -> vector2f:
        return self.m_position

    def getSize(self) -> vector2i:
        return vector2i(self.m_texture.get_width(), self.m_texture.get_height())
