import math

from game.point import Point
from game.entity.projectile import Projectile

def add_entity(cast, category, location, theta=0):
    if category == "projectile":
        entityType = Projectile(location.get_x(), location.get_y(), round(math.cos(theta) * 20), round(math.sin(theta) * 20))
    cast[category].append(entityType)