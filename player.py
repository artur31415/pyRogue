import math
import pygame


class Player:
    def __init__(self, position) -> None:
        self.position = position
        self.width = 20
    
    def get_points(center, radius, mouse_position):
        # calculate the normalized vector pointing from center to mouse_position
        length = math.hypot(mouse_position[0] - center[0], mouse_position[1] - center[1])
        # (note we only need the x component since y falls 
        # out of the dot product, so we won't bother to calculate y)
        angle_vector_x = (mouse_position[0] - center[0]) / length

        # calculate the angle between that vector and the x axis vector (aka <1,0> or i)
        angle = math.acos(angle_vector_x)

        # list of un-rotated point locations
        triangle = [0, (3 * math.pi / 4), (5 * math.pi / 4)]

        result = list()
        for t in triangle:
            # apply the circle formula
            x = center[0] + radius * math.cos(t + angle)
            y = center[1] + radius * math.sin(t + angle)
            result.append((x, y))

        return result

    def draw(self, surface):
        top_p = (self.position.x + self.width / 2, self.position.y)
        bottom_left_p = (self.position.x, self.position.y + self.width)
        bottom_right_p = (self.position.x + self.width, self.position.y + self.width)
        
        pygame.draw.polygon(surface, (100, 50, 100),[top_p, bottom_left_p, bottom_right_p])
