from game import constants
import arcade

class Entity(arcade.Sprite):

    def __init__(self, inEntity, inX, inY, inW, inH, inOrient, inVX = 0, inVY = 0):
        self.__x = inX
        self.__y = inY
        self.__vx = inVX
        self.__vy = inVY
        if inOrient:
            self.__w = inH
            self.__h = inW
        else:
            self.__w = inW
            self.__h = inH
        self.__type = inEntity
        super().__init__(inEntity)
        print(f"Created new {self.__type} entity with the following information: x:{self.__x}, y:{self.__y}, w:{self.__w}, h:{self.__h}")

    def getAttribute(self, attributeName="type"):
        if attributeName == "type": return self.__type
        elif attributeName == "x": return self.__x
        elif attributeName == "y": return self.__y
        elif attributeName == "w": return self.__w
        elif attributeName == "h": return self.__h
        elif attributeName == "v": return self.__vx, self.__vy

    def setPos(self, inX, inY):
        self.__x = inX
        self.__y = inY

    def changeVelocity(self, dX = 0, dY = 0):
        self.__vx = max(-1 * constants.playerSpeedLimit, min(self.__vx + dX, constants.playerSpeedLimit))
        self.__vy = max(-1 * constants.playerSpeedLimit, min(self.__vy + dY, constants.playerSpeedLimit))

    def draw(self):
        if self.__type == "rectangle":
            arcade.draw_rectangle_filled(self.__x, self.__y, self.__w, self.__h, arcade.color.GRAY)
            print(f"{self.__x}, {self.__y}")
        elif self.__type == "circle":
            arcade.draw_circle_filled(self.__x, self.__y, self.__w, arcade.color.RED)
        elif self.__type == "hcircle":
            arcade.draw_circle_outline(self.__x, self.__y, self.__w, arcade.color.DARK_YELLOW, 10)