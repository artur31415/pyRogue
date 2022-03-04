import math
import pygame


class Player:
    def __init__(self, position) -> None:
        self.position = position
        self.width = 20
        self.orientation = 0

    def apply_veclocity_mag(self, magnitude):
        vel = (magnitude * math.cos(self.orientation), magnitude * math.sin(self.orientation))
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
        # top_p = (self.position[0] + self.width / 2, self.position[1])
        # bottom_left_p = (self.position[0], self.position[1] + self.width)
        # bottom_right_p = (self.position[0] + self.width, self.position[1] + self.width)

        triangle_points = self.get_triangle_points()
        
        pygame.draw.polygon(surface, (100, 50, 100),triangle_points)
