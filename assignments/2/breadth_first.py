from path import Path, Node
from board import Board

class BreadthFirst:

    def __init__(self, starting_board):
        # initial node has no parent
        self.path = Path(Node(starting_board, None))

#    def search(self):
#        #expand first node
#        self.lastVisitedNodes = self.path.getLeafNodes()
#        for node in self.lastVisitedNodes:
#            if(node.data.board_completed()):
#                return True
#            for board in node.data.next():
#                node_new = Node(board, node)
#                node.addChild(node_new)
#                self.path.addLeaf(node_new)
#
#            self.path.addVisitedNode(node)
#
#        return False

    def search(self):
        #expand first node
        node = self.path.getFirstLeaf()
        if(node.data.board_completed()):
            return True
        for board in node.data.next():
            node_new = Node(board, node)
            node.addChild(node_new)
            self.path.addLeaf(node_new)

        self.path.addVisitedNode(node)

        return False

    def getLastPath(self):
        return self.path.getPath(self.path.getLastVisitedNode())
