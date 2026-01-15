import pygame
from Square import Square
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Pawn import Pawn

# board creater

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None
        self.turn = 'white'
        self.config = [
            'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR',
            'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP',
            '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '',
            'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP',
            'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR',
        ]
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        output = []
        for y in range(8):
            for x in range(8):
                output.append(Square(x, y, self.tile_width, self.tile_height))
        return output
    
    def setup_board(self):
        