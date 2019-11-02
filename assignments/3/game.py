from player import Player

class Game:

    def __init__(self, board, player1, player2):
        self.players = [player1, player2]
        self.board   = board

        self.currentPlayer = 0
        self.playerCount   = 2
        self.boardHistory = [self.board]

    def getCurrentPlayerMove(self):
        nextBoard = self.players[self.currentPlayer].getMove(self.board)
        self.currentPlayer += 1
        self.currentPlayer %= self.playerCount
        return nextBoard


    def playGame(self):
        """ Take turns having each player make a move
            returns the list of boards in the order they were played  """
        while(self.board.winner() is None):
            self.board = self.getCurrentPlayerMove()
            self.boardHistory.append(self.board)
        return self.boardHistory


