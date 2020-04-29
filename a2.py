from cvs import *

EMPTY_TILE = "tile"
START_PIPE = "start"
END_PIPE = "end"
LOCKED_TILE = "locked"

SPECIAL_TILES = {
    "S": START_PIPE,
    "E": END_PIPE,
    "L": LOCKED_TILE
}

PIPES = {
    "ST": "straight",
    "CO": "corner",
    "CR": "cross",
    "JT": "junction-t",
    "DI": "diagonals",
    "OU": "over-under"
}

### add code here ###

class PipeGame:
    """
    A game of Pipes.
    """
    def __init__(self, game_file='game_1.csv'):
        """
        Construct a game of Pipes from a file name.

        Parameters:
            game_file (str): name of the game file.
        """
        #########################COMMENT THIS SECTION OUT WHEN DOING load_file#######################
        board_layout = [[Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True)], [StartPipe(1), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True), Tile('tile', True)], [Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Pipe('junction-t', 0, False), Tile('tile', True), Tile('tile', True)], [Tile('tile', True), \
        Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('locked', False), Tile('tile', True)], \
        [Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), EndPipe(3), \
        Tile('tile', True)], [Tile('tile', True), Tile('tile', True), Tile('tile', True), Tile('tile', True), \
        Tile('tile', True), Tile('tile', True)]]

        playable_pipes = {'straight': 1, 'corner': 1, 'cross': 1, 'junction-t': 1, 'diagonals': 1, 'over-under': 1}
        #########################COMMENT THIS SECTION OUT WHEN DOING load_file#######################
        end_pipe_position = self.end_pipe_positions()

    def get_board_layout(self) -> list<list<Tile>>:
        #Returns a list of lists that are representations of the rows and columns
        print(str(self.board_layout))
    
    def get_playable_pipes(self) -> (dict<str:int>):
        #Returns a dictionary of all playable pipes types and number of available pipes per type
        #TO-DO: Code
        print(str(self.playable_pipes))

    def change_playable_amount(self, pipe_name: str, number: int):
        #Add the quantity of playable pipes to type specified by pipe_name to number (in the selection panel)
        #TO-DO: Code
        for i in self.playable_pipes:
            if self.playable_pipes[i] == pipe_name:
                self.playable_pipes[i] += number
        return self.playable_pipes

    def get_pipe(self, position) -> (Pipe|Tile):
        #Returns the Pipe at the position or the tile if there is no pipe at that position
        #TO-DO: Code
        print(str(self.board_layout[position]))

    def set_pipe(self, pipe: Pipe, position: tuple<int, int>):
        #Place the specified pipe at the given position (row, col) in the game board. The number of available pipes of the relevant type should also be updated
        #TO-DO: Code
        self.board_layout[position] = pipe
        return self.board_layout[position]

    def pipe_in_position(self, position) -> Pipe:
        #Returns the pipe in the given position (row, col) of the game board if there is a Pipe in the given position. Reutrns None if the position given is None or if the object in the given position is not a Pipe.
        #TO-DO: Code
        if self.board_layout[position] == Pipe:
            print self.board_layout[position]
        else
            print None

    def remove_pipe(self, position: tuple<int, int>):
        #Removes the pipe at the given position from the board by creating an empty tile at the given (row, col) position and increasing the playable number of the given Pipe
        #TO-DO: Code
    
        for i in PIPES:
            if PIPES[i] == self.board_layout[position]:
                self.playable_pipes += 1
        self.board_layout[position] = Tile('tile', True)


    def position_in_direction(self, direction, position) -> tuple<str, tuple<int, int>>:
        #Returns the direction and position (row, col) iun the given direction from the given position, if the resulting position is valid within the game grid. Returns None if the resulting position is invalid.
        #TO-DO: Code
        if direction == 'E':
            self.board_layout[position] += (0, 1)
            print(str('W', self.board_layout[position]))
        elif direction == 'W':
            self.board_layout[position] -= (0, 1)
            print(str('E', self.board_layout[position]))
        elif direction == 'N':
            self.board_layout[position] += (1, 0)
            print(str('N', self.board_layout[position]))
        elif direction == 'S':
            self.board_layout[position] -= (1, 0)
            print(str('S', self.board_layout[position]))

    def end_pipe_positions(self):
        #Find and save the start and end positions from the game board. Called in init() so the positions can be found when PipeGame class is constructed.
        #TO-DO: Code
        temp = [[], []]
        for i, j in self.board_layout:
            if self.board_layout[i, j] == StartPipe():
                temp[0] = self.board_layout[i, j]
            elif self.board_layout[i, j] == EndPipe():
                temp[1] = self.board_layout[i, j]
        return temp


    def get_starting_position(self) -> (tuple<int, int>):
        #Returns the (row, col) position of the start pipe.
        #TO-DO: Code
        for i, j in self.board_layout:
            if self.board_layout[i, j] == StartPipe():
                temp = (i, j)
                print(str(temp))
        

    def get_ending_position(self) -> (tuple<int, int>):
        #Returns the (row, col) position of the end pipe.
        #TO-DO: Code
         for i, j in self.board_layout:
            if self.board_layout[i, j] == EndPipe():
                temp = (i, j)
                print(str(temp))

        

    def check_win(self):
        #(bool) Returns True  if the player has won the game False otherwise.
        
        position = self.get_starting_position()
        pipe = self.pipe_in_position(position)
        queue = [(pipe, None, position)]
        discovered = [(pipe, None)]
        while queue:
            pipe, direction, position = queue.pop()
            for direction in pipe.get_connected(direction):
                if self.position_in_direction(direction, position) is None:
                    new_direction = None 
                    new_position = None
                else:
                    new_direction, new_position = self.position_in_direction(direction, position)
                    if new_position == self.get_ending_position() and direction == self.pipe_in_position(
                        new_position).get_connected()[0]:
                        return True

                pipe = self.pipe_in_position(new_position)
                if pipe is None or (pipe, new_direction) in discovered:
                    continue
                discovered.append((pipe, new_direction))
                queue.append((pipe, new_direction, new_position))
        return False

class Tile:
# The Tile class, for available space on the Game Board
    def __init__(self, name: str, selectable: bool = True):
        #TO-DO: Code
        self.name = name
        self.selectable = selectable

    def get_name(self) -> str:
        #Returns the name of the Tile
        #TO-DO: Code
        print(str(self.name))

    def get_id(self) -> str:
        #Returns ID of the Tile class
        #TO-DO: Code
        print('tile')

    def set_select(self, select: bool):
        #Sets status of the select switch to True or False
        #TO-DO: Code
        self.selectable = select
        return self.selectable

    def can_select(self) -> bool:
        #Returns True if tile is selectable, or False if not selectable
        #TO-DO: Code
        print(str(self.selectable))

    def _str_(self) -> str:
        #Returns the string representation of the Tile
        #TO-DO: Code
        print(str(self.name, self.selectable))

    def _repr_(self) -> str:
        #Same as str(self)
        #TO-DO: Code
        print(str(self.name, self.selectable))
    
class Pipe:
# The Pipe class, represents a Pipe in the Game
    def __init__(self, name: str, orientation: int = 0, selectable: bool = True):
        #TO-DO: Code
        self.name = name
        self.orientation = orientation
        self.selectable = selectable

    def get_connected(self, side: str) -> list<str>:
        #Returns a list of all sides that are connected to the given side, i.e. return a list containing some combination of 'N', 'S', 'E', 'W', or an empty list
        #TO-DO: Code
        temp = []
        for i in self.orientation:
            if self.orientation == 0 and side == 'N':
                temp[0] == 'S'
            elif self.orientation == 0 and side 'S':
                temp[0] == 'N'
            elif self.orientation == 1 and side == 'E':
                temp[0] == 'W'
            elif self.orientation == 1 and side == 'W':
                temp[0] == 'E'
            elif self.orientation == 2 and side == 'N':
                temp[0] ==  'S'
            elif self.orientation == 2 and side == 'S':
                temp[0] == 'N'
            elif self.orientation == 3 and side == 'E':
                temp[0] == 'W'
            elif self.orientation == 3 and side == 'W':
                temp[0] == 'E'
        return temp
    def rotate(self, direction: int):
        #Rotates the pipe one turn. Positive means clockwise, negative means counter-clockwise, 0 means no rotation
        #TO-DO: Code
        self.orientation += direction
        return self.orientation

    def get_orientation(self) -> int:
        #Returns the orientation of the pipe (orientation must be in the range [0, 3])
        #TO-DO: Code
        print(str(self.orientation))

    def _str_(self) -> str:
        #Returns the string representation of the Pipe
        #TO-DO: Code
        print(str(self.name, self.orientation, self.selectable))

    def _repr_(self) -> str:
        #Same as str(self)
        #TO-DO: Code
        print(str(self.name, self.orientation, self.selectable))

class SpecialPipe:
# Abstract class to represent starting and ending pipes in the game
    def _str_(self) -> str:
        #Returns the string representation of the Special Pipe
        print(str(self.name, self.orientation, self.selectable))

    def _repr_(self) -> str:
        #Same as str(self)
        #TO-DO: Code
        print(str(self.name, self.orientation, self.selectable))

class StartPipe:
# The starting pipe in a game of Pipe
    def __init__(self, orientation: int = 0):
        #TO-DO: Code
        self.name = name
        self.orientation = orientation

    def get_connected(self, side=None) -> list<str>:
        #Returns the direction that the start pipe is facing
        #TO-DO: Code
        temp = []
        if self.orientation == 0:
            temp[0] = 'S'
        elif self.orientation == 1:
            temp[0] = 'W'
        elif self.orientation == 2:
            temp[0] = 'N'
        elif self.orientation == 3:
            temp[0] = 'E'
        return temp

    def __str__(self) -> str:
        print(srt(self.name, self.orientation))

    def __repr__(self) -> str:
        print(srt(self.name, self.orientation))

class EndPipe:
# The ending pipe in a game of Pipe
    def __init__(self, orientation: int = 0):
        #TO-DO: Code
        self.name = name
        self.orientation = orientation

    def get_connected(self, side=None) -> list<str>:
        #Returns the direction that the end pipe is facing
        #TO-DO: Code
        temp = []
        if self.orientation == 0:
            temp[0] = 'S'
        elif self.orientation == 1:
            temp[0] = 'W'
        elif self.orientation == 2:
            temp[0] = 'N'
        elif self.orientation == 3:
            temp[0] = 'E'
        return temp
    
    def __str__(self) -> str:
        print(srt(self.name, self.orientation))

    def __repr__(self) -> str:
        print(srt(self.name, self.orientation))


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
