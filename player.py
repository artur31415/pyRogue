import math
import pygame


class Player:
    def __init__(self, position) -> None:
        self.position = position
        self.width = 20
        self.orientation = 0
        self.energy = 100

    def shoot(self):
        return self.get_position_normal()

    def get_position_normal(self):
        return (math.cos(self.orientation), math.sin(self.orientation))

    def apply_veclocity_mag(self, magnitude):
        normal = self.get_position_normal()
        vel = (magnitude * normal[0], magnitude * normal[1])
        self.position = (self.position[0] + vel[0], self.position[1] + vel[1])
    
    def get_triangle_points(self):
        # list of un-rotated point locations
        triangle = [0, (3 * math.pi / 4), (5 * math.pi / 4)]

        result = list()
        for t in triangle:
            # apply the circle formula
            x = self.position[0] + self.width * math.cos(t + self.orientation)
            y = self.position[1] + self.width * math.sin(t + self.orientation)
            result.append((x, y))

        return result

    def draw(self, surface):
        triangle_points = self.get_triangle_points()
        
        pygame.draw.polygon(surface, (100, 50, 100),triangle_points)
