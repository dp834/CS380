from player import Player

class HumanPlayer(Player):

    def getMove(self, board):
        nextBoard = board.clone()
        print(" 1234")
        print(board)
        print("Playing for {}".format(self.label))

        while(board.equals(nextBoard)):
            try:
                nextBoard.place(int(input("Enter the column to place your piece:")) - 1, self.label)
            except:
                pass
        return nextBoard

