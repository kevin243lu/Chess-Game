import pygame

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width # makes sure the tile stays inside the game window
        self.abs_y = y * height # makes sure the tile stays inside the game window
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10) # highlights possible moves
        self.occupying_square = None
        self.coord = self.get_coord() # gives back the coords for the tile ie. a4, g6
        self.highlight = False
        self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

    # gets the coord
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)
    
    # configures the tile to match light/dark/highlighted
    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)