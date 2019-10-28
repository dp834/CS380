from path import Path, Node
from board import Board
import random

class RandomWalk:

    def __init__(self, starting_board):
        # initial node has no parent
        self.Path = Path(Node(starting_board, None))

    def expand_random_node(self):
        node = self.Path.getCurrentNode()
        if(node.data.board_completed()):
            return

        if(not isinstance(node.getData(), Board)):
            print("Node is not a board")
            return None
        node.addChildren(node.getData().next())
        self.Path.setCurrentNode(random.choice(node.getChildren()))

    def walk_n_nodes(self, number):
        for i in range(number - 1):
            self.expand_random_node()
        return self.Path.getPath(self.Path.getCurrentNode())
