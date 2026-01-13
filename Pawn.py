import pygame

from Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def get_possible_moves(self):
        output = []
        moves = []
        # move forward
        if self.color == 'white':
            moves.append((0, 1))
            if not self.has_moved:
                moves.append(0, 2)
        elif self.color == 'black':
            moves.append((0, -1))
            if not self.has_moved:
                moves.append(0, -2)
        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0:
                output.append()