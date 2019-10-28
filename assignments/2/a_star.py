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
    for i in range(car_pos[1][0] + 1, data.goal[0]):
        if(data.board[i][data.goal[1]] != data.empty_char):
            cars = cars + 1
    return distance + cars

class AStar:

    def __init__(self, starting_board):
        # initial node has no parent
        self.path = Path(Node(starting_board, None))

    def search(self):
        #expand first node
        node = self.path.getSmallestCostLeaf(heuristic)

        if(self.path.alreadyVisited(node)):
            return False

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

