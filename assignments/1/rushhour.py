#!/usr/bin/python3

import sys # for command line arguments
from board import Board, print_boards

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

    if(command == "print"):
        board = Board(optional_arg)
        board.show()
    elif(command == "done"):
        board = Board(optional_arg)
        print(board.board_completed())
    elif(command == "next"):
        board = Board(optional_arg)
        print_boards(board.next_boards())

    else:
        print("Unknown command {}".format(command))



if(__name__ == "__main__"):
    main()
