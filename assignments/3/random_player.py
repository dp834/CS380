from player import Player
import random

class RandomPlayer(Player):

    def getMove(self, board):
        return random.choice(self.getNextMoves(board))
