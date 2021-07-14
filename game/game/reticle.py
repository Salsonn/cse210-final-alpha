from game.point import Point

class Reticle():

    def __init__(self):
        self._reticle = Point(0, 0)
        self._reticle_dx = 0
        self._reticle_dy = 0

    def set_reticle(self, point, dx=0, dy=0):
        self._reticle = point
        self._reticle_dx = dx
        self._reticle_dy = dy

    def get_reticle(self):
        return self._reticle

    def get_reticleX(self):
        return self._reticle.get_x()

    def get_reticleY(self):
        return self._reticle.get_y()

    def get_reticle_dx(self):
        return self._reticle_dx

    def get_reticle_dy(self):
        return self._reticle_dy