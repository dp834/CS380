from path import Path, Node
from board import Board

def sortByCost(nodes):
   sorted(nodes, key=lambda x: x.getCost(heuristic))

# take the distance the car is to the exit plus the number of other cars along it's path
def heuristic(data):
    if(data is None):
        return 0
    if(not isinstance(data, Board)):
        print("Hueristic got non Board type")
    car_pos = data.find_car_bounds(data.main_car)
    distance = data.goal[0] - car_pos[1][0]
    cars = 0
    for i in range(car_pos[1][0] + 1, data.goal[0] + 1):
        if(data.board[i][data.goal[1]] != data.empty_char):
            cars += 1
            # cars that are blocking the car that needs to move
            data.show()
            cars += car_blocked(data, data.board[i][data.goal[1]], (i, data.goal[1]))
    return distance + cars

def car_blocked(board, car, pos):
    if( car == board.empty_char):
        return 0

    start, end = board.find_car_bounds(car)

    if(start[0] == end[0]):
        piecesBefore = abs(start[1] - pos[1])
        piecesAfter  = abs(end[1] - pos[1])
        if(start[1] == 0):
            previousOccupied = 0
        else:
            previousOccupied = start[1] - 1

        while(previousOccupied > 0 and board.board[start[0]][previousOccupied] == board.empty_char):
            previousOccupied -= 1
        spacesBefore = start[1] - previousOccupied - 1
        carBefore = (start[0], previousOccupied)

        if(end[1] == len(board.board[1]) - 1):
            nextOccupied = end[1]
        else:
            nextOccupied = end[1] + 1

        while(nextOccupied < len(board.board[0]) - 1 and board.board[end[0]][nextOccupied] == board.empty_char):
            nextOccupied += 1
        spacesAfter = nextOccupied - end[1] - 1
        carAfter = (end[0], nextOccupied)

    if(start[1] == end[1]):
        piecesBefore = abs(start[0] - pos[0])
        piecesAfter  = abs(end[0] - pos[0])
        if(start[0] == 0):
            previousOccupied = 0
        else:
            previousOccupied = start[0] - 1

        while(previousOccupied > 0 and board.board[previousOccupied][start[1]] == board.empty_char):
            previousOccupied -= 1
        spacesBefore = start[0] - previousOccupied - 1
        carBefore = (previousOccupied, start[1])

        if(end[0] == len(board.board) - 1):
            nextOccupied = end[0]
        else:
            nextOccupied = end[0] + 1

        while(nextOccupied < len(board.board) - 1 and board.board[nextOccupied][end[1]] == board.empty_char):
            nextOccupied += 1
        spacesAfter = nextOccupied - end[0] - 1
        carAfter = (nextOccupied,end[1])
    print("car {} cars {} {}".format(car, board.board[carBefore[0]][carBefore[1]], board.board[carAfter[0]][carAfter[1]]))
    print("piecesBefore {} spacesAfter {} piecesAfter {} spacesBefore {}".format(piecesBefore, spacesAfter, piecesAfter, spacesBefore))
    if(piecesBefore >= spacesAfter):
        if(piecesAfter >= spacesBefore):
            if(board.board[carBefore[0]][carBefore[1]] in [car, board.empty_char]):
                costAfter  = car_blocked(board, board.board[carAfter[0]][carAfter[1]], carAfter)
                print("{} A {}".format(car, costAfter))
                return 1 + costAfter

            if(board.board[carAfter[0]][carAfter[1]] in [car, board.empty_char]):
                costBefore = car_blocked(board, board.board[carBefore[0]][carBefore[1]], carBefore)
                print("{} B {}".format(car, costBefore))
                return 1 + costBefore

            costBefore = car_blocked(board, board.board[carBefore[0]][carBefore[1]], carBefore)
            costAfter  = car_blocked(board, board.board[carAfter[0]][carAfter[1]], carAfter)
            print("{} B {} A {}".format(car, costBefore, costAfter))
            return 1 + min([costBefore, costAfter])

    return 0



class AStar:

    def __init__(self, starting_board):
        # initial node has no parent
        self.path = Path(Node(starting_board, None))

    def search(self):
        #expand first node
        node = self.path.getSmallestCostLeaf(heuristic)

        while(self.path.alreadyVisited(node)):
            node = self.path.getSmallestCostLeaf(heuristic)

        self.path.addVisitedNode(node)

        if(node.data.board_completed()):
            return True

        for board in node.data.next():
            node_new = Node(board, node)
            node.addChild(node_new)
            self.path.addLeaf(node_new)


        return False

    def getLastPath(self):
        return self.path.getPath(self.path.getLastVisitedNode())

    def getVisitedCount(self):
        return self.path.getVisitedCount()

