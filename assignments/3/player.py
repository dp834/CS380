import abc

class Player:

    def __init__(self, label):
        self.label = label

    def getNextMoves(self, board):
        return board.next(self.label)

    @abc.abstractmethod
    def getMove(self, board):
        """ return board of move to make """
        return
