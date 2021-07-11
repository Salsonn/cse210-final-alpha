import math

from game import constants

from game.point import Point
from game.entity.projectile import Projectile

def add_entity(entities, category, location, theta=0):
    if category == "projectile":
        entityType = Projectile(location.get_x(), location.get_y(), round(math.cos(theta) * constants.projectileSpeed), round(math.sin(theta) * constants.projectileSpeed))
    entities[category].append(entityType)