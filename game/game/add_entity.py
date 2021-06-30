import math

from game.point import Point
from game.entity.projectile import Projectile

def add_entity(cast, category, location, theta=0):
    if category == "projectile":
        entityType = Projectile(location.get_x(), location.get_y(), math.cos(theta) * 10, math.sin(theta) * 10)
    cast[category].append(entityType)