#!/usr/bin/python3

import sys # for command line arguments
from board import Board, print_boards, print_boards_with_max
from random_walk import RandomWalk
from breadth_first import BreadthFirst

def main():
    argcount = len(sys.argv)
    command = None
    optional_arg = None

    if(argcount == 2):
        command = sys.argv[1]
        optional_arg = "  o aa|  o   |xxo   |ppp  q|     q|     q"
    elif(argcount == 3):
        command = sys.argv[1]
        optional_arg = sys.argv[2]
    else:
        print("Invalid parameters\nUsage: {} <command> [<optional-argument>]".format(sys.argv[0]))

    board = Board(optional_arg)

    if(command == "print"):
        board.show()
    elif(command == "done"):
        print(board.board_completed())
    elif(command == "next"):
        print_boards(board.next_boards())
    elif(command == "random"):
        walk = RandomWalk(board)
        path = walk.walk_n_nodes(10)
        print_boards_with_max(path, 6)
    elif(command == "bfs"):
        bfs = BreadthFirst(board)
        searches = 0
        while(bfs.search() == False and searches < 100000):
            searches = searches + 1
            print_boards_with_max(bfs.getLastPath(), 6)
            print(searches)
        print_boards_with_max(bfs.getLastPath(), 6)
        print(searches)



    else:
        print("Unknown command {}".format(command))



if(__name__ == "__main__"):
    main()
