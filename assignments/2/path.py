import copy

class Path:
    def __init__(self, currentNode=None):
        self.currentNode = currentNode
        self.visitedNodes = []
        self.leafNodes = []
        if(currentNode is not None):
            self.leafNodes.append(currentNode)

    def addLeaf(self, node):
        if(not isinstance(node, Node)):
            print("Must add Node to path")
            return None

        self.leafNodes.append(node)

    def addVisitedNode(self, node):
        self.visitedNodes.append(node)

    def getPath(self, node):
        path = []
        while(node is not None):
            path.append(node.getData())
            node = node.getParent()
        path.reverse()
        return path

    def setCurrentNode(self, node):
        if(not isinstance(node,Node)):
            print("Current Node must be of type Node")
            return None
        self.currentNode = node

    def getCurrentNode(self):
        return self.currentNode

    def getFirstLeaf(self):
        if(len(self.leafNodes) == 0):
            print("No more leaf Nodes")
            return None
        return self.leafNodes.pop(0)

    def getLeafNodes(self):
        nodes = self.leafNodes
        self.leafNodes = []
        return nodes

    def sortLeafNodes(self, sortingFunction):
        sortingFunction(self.leafNodes)

    def getLastVisitedNode(self):
        if(len(self.visitedNodes) == 0 ):
            print("No nodes visited")
            return None
        return self.visitedNodes[-1]

    def alreadyVisited(self, node):
        return node in self.visitedNodes

    def getVisitedCount(self):
        return len(self.visitedNodes)

    def getSmallestCostLeaf(self, heuristic):
        node = min(self.leafNodes, key=lambda x: x.getCost(heuristic))
        self.leafNodes.remove(node)
        return node

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = []
        self.cost = None

    def __eq__(self, other):
        if(not isinstance(other,Node)):
            return False
        return self.data == other.data

    def getParent(self):
        return self.parent

    def addChildren(self, dataList):
        for data in dataList:
            self.children.append(Node(data, self))

    def addChild(self, node):
        self.children.append(node)

    def getChildren(self):
        return self.children

    def getData(self):
        return self.data

    def getLength(self):
        if(self.getParent() is None):
            return 0
        return 1 + self.getParent().getLength()

    def getCost(self, heuristic):
        if(self.cost != None):
            return self.cost
        if(self.getParent() == None):
            return 0
        self.cost = self.getParent().getLength() + heuristic(self.data)
        return self.cost

