from hex import Hex

class Board:
    def __init__(self):
        # board is a 2d array of Hex objects
        self.board = self.generate_random_board()

    def get_hex(self, row, col):
        return self.board[row][col]

    def generate_random_board(self):
        # board is 7 rows, the amount of columns differ for each row
        board = []
        num_of_cols = [4, 5, 6, 7, 6, 5, 4]
        for i in range(7):
            row = []
            cols = num_of_cols[i]
            for j in range(cols):
                if j == 3 and i == 3:
                    row.append(Hex.generate_desert_hex(i, j))
                elif i == 0 or i == 6 or j == 0 or j == cols - 1:
                    if Board.is_harbor_coordinate(i, j):
                        row.append(Hex.generate_random_harbor_hex(i, j))
                    else:
                        row.append(Hex.generate_water_hex(i, j))
                else:
                    row.append(Hex.generate_random_resource_hex(i, j))
            board.append(row)
        return board

    def is_harbor_coordinate(i, j):
        # middle of top and bottom rows
        if (i == 0 and j == 2) or (i == 6 and j == 2):
            return True
        # left half of board
        elif i % 2 == 0:
            if j == 0:
                return True
        # right half
        elif (i == 1 and j == 4) or (i == 3 and j == 6) or (i == 5 and j == 4):
            return True
        return False 

    def __str__(self):
        string = "\n"
        for i in range(len(self.board)):
            row = str(self.board[i])
            left_margin = (3 - i) * 6 if i <=3 else (i - 3) * 6
            spaces = " " * left_margin
            string += spaces + row + "\n"
        return string

    def draw(self, screen):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                hex = self.board[row][col]
                hex.draw(screen)
