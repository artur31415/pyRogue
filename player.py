import pygame


class Player:
    def __init__(self, position) -> None:
        self.position = position
        self.width = 20

    def draw(self, surface):
        top_p = (self.position.x + self.width / 2, self.position.y)
        bottom_left_p = (self.position.x, self.position.y + self.width)
        bottom_right_p = (self.position.x + self.width, self.position.y + self.width)
        
        pygame.draw.polygon(surface, (100, 50, 100),[top_p, bottom_left_p, bottom_right_p])
