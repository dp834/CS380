import copy
import itertools

class Board:

    def __init__(self, string, goal=(5,2), main_car="x", empty_char=" "):
        # our board will be accessed by (x, y) where x is the
        # column and y is the row and they are zero indexed
        # (0, 0) is the upper left corner
        # (2,3) =
        # xxxxxx
        # xxxxxx
        # xxxxxx
        # xx0xxx
        # xxxxxx
        # xxxxxx
        self.board = [[None]*6 for _ in range(6)]
        self.goal  = goal
        self.main_car= main_car
        self.empty_char=" "
        self.cars = [self.main_car]
        self.create_from_string(string)

    def create_from_string(self, string):
        lines = string.split("|")
        self.columns = len(lines[0])
        self.rows = len(lines)
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                self.board[j][i] = char
                if(char not in self.cars and char != self.empty_char):
                    self.cars.append(char)

    def show(self):
        print("-"*(len(self.board) + 2))
        for i in range(len(self.board)):
            if(self.goal == (0, i)):
                print(" ", end="")
            else:
                print("|", end="")
            for j in range(len(self.board[i])):
                print(self.board[j][i], end="")
            if(self.goal == (j, i)):
                print(self.empty_char)
            else:
                print("|")
        print("-"*(len(self.board) + 2))

    def show_line(self, line):
        if(self.goal == (0, line)):
            print(" ", end="")
        else:
            print("|", end="")
        for j in range(len(self.board[line])):
            print(self.board[j][line], end="")
        if(self.goal == (j, line)):
            print(self.empty_char, end="")
        else:
            print("|", end="")

    def find_car_bounds(self, car):
        start = (-1, -1)
        end = -1
        for i, line in enumerate(self.board):
            try:
                start = (i, line.index(car))
            except:
                pass
            if(start[0] != -1):
                break
        if(-1 in start):
            print("Couldn't find car {} in current board".format(car))
            return None
        end = copy.deepcopy(start)
        # look as far right as possible
        while(end[0] < 5 and self.board[end[0]+1][end[1]] == car):
            end = (end[0] + 1, end[1])
        if(start != end):
            return (start, end)
        # look as far down as possible
        while(end[1] < 5 and self.board[end[0]][end[1]+1] == car):
            end = (end[0], end[1] + 1)
        if(start != end):
            return (start, end)
        # car is of size 1
        return None

    def next_for_car(self, car):
        # with the car bound we just add/subtract to the coordinate that is not the same
        start, end = self.find_car_bounds(car)
        newBoards = []
        boardCopy = copy.deepcopy(self)
        if(start[0] == end[0]):
            #start by decrementing
            spaces = 1
            while(start[1]-spaces >= 0 and self.board[start[0]][start[1]-spaces] == self.empty_char):
                boardCopy.board[start[0]][start[1]-spaces] = car
                boardCopy.board[end[0]][end[1]-spaces+1] = self.empty_char
                newBoards.append(boardCopy)
                boardCopy = copy.deepcopy(boardCopy)
                spaces = spaces + 1
            # now increment
            spaces = 1
            boardCopy = copy.deepcopy(self)
            while(end[1]+spaces < len(self.board[0]) and self.board[end[0]][end[1]+spaces] == self.empty_char):
                boardCopy.board[end[0]][end[1]+spaces] = car
                boardCopy.board[start[0]][start[1]+spaces-1] = self.empty_char
                newBoards.append(boardCopy)
                boardCopy = copy.deepcopy(boardCopy)
                spaces = spaces + 1
        elif(start[1] == end[1]):
            #start by decrementing
            spaces = 1
            while(start[0]-spaces >= 0 and self.board[start[0]-spaces][start[1]] == self.empty_char):
                boardCopy.board[start[0]-spaces][start[1]] = car
                boardCopy.board[end[0]-spaces+1][end[1]] = self.empty_char
                newBoards.append(boardCopy)
                boardCopy = copy.deepcopy(boardCopy)
                spaces = spaces + 1
            # now increment
            spaces = 1
            boardCopy = copy.deepcopy(self)
            while(end[0]+spaces < len(self.board) and self.board[end[0]+spaces][end[1]] == self.empty_char):
                boardCopy.board[end[0]+spaces][end[1]] = car
                boardCopy.board[start[0]+spaces-1][start[1]] = self.empty_char
                newBoards.append(boardCopy)
                boardCopy = copy.deepcopy(boardCopy)
                spaces = spaces + 1

        else:
            print("Invalid car bound")
            return None
        return newBoards

    def next_boards(self):
        # Need to join the sub-arrays
        return list(itertools.chain(*[self.next_for_car(car) for car in self.cars]))

    def next(self):
        return self.next_boards()

    def board_completed(self):
        return self.board[self.goal[0]][self.goal[1]] == self.main_car


def print_boards(boards):
    # get height of the board and add 2 for the decorating lines
    if(len(boards)==0):
        return
    print("-------- "*len(boards))
    for i in range(len(boards[0].board)):
        for board in boards:
            board.show_line(i)
            print(" ",end="")
        print()
    print("-------- "*len(boards))

