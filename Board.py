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
    
    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
    
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_from_pos((x, y))
                    # looking to see what piece the square has
                    if piece[1] == 'R':
                        square.occupying_piece = Rook((x, y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'N':
                        square.occupying_piece = Knight((x, y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'B':
                        square.occupying_piece = Bishop((x, y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'Q':
                        square.occupying_piece = Queen((x, y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'K':
                        square.occupying_piece = King((x, y), 'white' if piece[0] == 'w' else 'black', self)
                    elif piece[1] == 'P':
                        square.occupying_piece = Pawn((x, y), 'white' if piece[0] == 'w' else 'black', self)

    def handle_click(self, mx, my):
        # allows us to click inside the game window
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if self.selected_piece is None: # shows the piece you have clicked on
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'white' if self.turn == 'black' else 'black'
        elif clicked_square.occupying_piece is not None:
            if clicked_square.occupying_piece.color == self.turn:
                self.selected_piece = clicked_square.occupying_piece

    # game state checker
    def is_in_check(self, color, pos):
        output = False
        king_pos = None
        changing_piece = None
        old_square = None
        new_square = None
        new_square_old_piece = None
        if board_change is not None:
            for square in self.squares:
                if square.pos == board_change[0]:
                    changing_piece = square.occupying_piece
                    old_square = square
                    