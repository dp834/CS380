from player import Player


class MinimaxPlayer(Player):

    def __init__(self, label):
        super().__init__(label)
        self.opponentLabel = "O" if self.label == "X" else "X"

    def getMove(self, board):
        """ return board of move to make """
        return self.playMinimax(board)

    def playMinimax(self, board):
        """
            minimax_decision
            return the state maximizing the minimized utility function

            input: State
            returns: action (newState)
        """
        moves = []
        for b in board.next(self.label):
            moves.append( (b, self.minimize(b, 1)) )
        move = max(moves, key=(lambda x: x[1]))
        moves.sort(key=(lambda x: x[1]))
        return move[0]


    def maximize(self, board, depth):
        winner = board.winner()
        if(winner is not None):
            return self.utility(winner, depth)

        maximum = -1
        for b in board.next(self.label):
            maximum = max([maximum, self.minimize(b, depth + 1)])

        return maximum

    def minimize(self, board, depth):
        winner = board.winner()
        if(winner is not None):
            return self.utility(winner, depth)

        minimum = 2
        for b in board.next(self.opponentLabel):
            minimum = min([minimum, self.maximize(b, depth + 1)])

        return minimum

    def utility(self, winner, depth):
        if(winner == "TIE"):
            return 0
        if(winner == self.label):
            #winning sooner is better
            return 1/depth
        if(winner is not None):
            #losing later is better
            return -1/depth

def printMinimaxMoves(moves):
    print("*"*20)
    for move in moves:
        print(move[1])
        print(move[0])
        print("----------------")
    print("*"*20)
