from player import Player


class MinimaxAlphaBetaPlayer(Player):

    def __init__(self, label):
        super().__init__(label)
        self.opponentLabel = "O" if self.label == "X" else "X"

    def getMove(self, board):
        """ return board of move to make """
        return self.playAlphaBeta(board)

    def playAlphaBeta(self, board):
        """
            minimax_decision
            return the state maximizing the minimized utility function

            input: State
            returns: action (newState)
        """
        moves = []
        self.tree = []
        for b in board.next(self.label):
            moves.append( (b, self.minimizeAlphaBeta(b, -1*float("inf"), float("inf"), 1)) )
        move = max(moves, key=(lambda x: x[1]))
        moves.sort(key=(lambda x: x[1]))
        self.tree.sort(key=(lambda x: x[0]))
        return move[0]


    def maximizeAlphaBeta(self, board, alpha, beta, depth):
        winner = board.winner()
        if(winner is not None):
            return self.utility(winner, depth)

        maximum = -1*float("inf")
        for b in board.next(self.label):
            asdf = self.minimizeAlphaBeta(b, alpha, beta, depth + 1)
            self.tree.append((depth, asdf, b))
            maximum = max([maximum, asdf])
            if(maximum > beta):
                return maximum
            alpha = max([alpha, maximum])

        return maximum

    def minimizeAlphaBeta(self, board, alpha, beta, depth):
        winner = board.winner()
        if(winner is not None):
            return self.utility(winner, depth)

        minimum = float("inf")
        for b in board.next(self.opponentLabel):
            asdf = self.maximizeAlphaBeta(b, alpha, beta, depth + 1)
            self.tree.append((depth, asdf, b))
            minimum = min([minimum, asdf])
            if(minimum < alpha):
                return minimum
            beta = min([beta, minimum])

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
        print(move[0])
        print(move[1])
