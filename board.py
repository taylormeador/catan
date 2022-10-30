from hex import Hex, Vertex, Edge

class Board:
    def __init__(self):
        # board is a 2d array of Hex objects
        self.board = self.generate_random_board()
        self.set_neighbors()
        self.set_vertices()
        self.set_edges()

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

    def draw(self, screen):
        # draw hexes, then roads, then cities/settlements
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                hex = self.board[row][col]
                hex.draw(screen)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                hex = self.board[row][col]
                # hex.draw_buildings(screen)

    def set_neighbors(self):
        # called when board is initialized
        # loop through all hexes add neighboring hexes to hex.neighbors 
        # TODO this only works 100% correctly for resource tiles. 
        # There are edge cases pertaining to water/harbor hexes that I might fix later
        for row in range(len(self.board)):
            even = row % 2 == 0
            row_len = len(self.board[row])
            row_above, row_below = None, None
            above_shorter, below_shorter = False, False
            if row:
                row_above = self.board[row - 1]
                above_shorter = len(row_above) < row_len
            if row < len(self.board) - 1:
                row_below = self.board[row + 1]
                below_shorter = len(row_below) < row_len

            for col in range(row_len):
                hex = self.board[row][col]

                # target columns can be left or right or above
                target_col_0 = col + 0 if above_shorter else col + 1
                target_col_2 = col + 0 if below_shorter else col + 1
                target_col_3 = col + -1 if below_shorter else col + 0
                target_col_5 = col + -1 if above_shorter else col + 0

                # left and right neighbors
                if col < row_len - 1:
                    hex.neighbors[1] = self.board[row][col + 1]
                if col:
                    hex.neighbors[4] = self.board[row][col - 1]

                # neighbors 0 and 5 
                if row_above:
                    if col < len(row_above) - 1:
                        hex.neighbors[0] = self.board[row - 1][target_col_0]
                    if col: 
                        hex.neighbors[5] = self.board[row - 1][target_col_5]

                # neighbors 2 and 3
                if row_below:
                    if col < len(row_below) - 1:
                        hex.neighbors[2] = self.board[row + 1][target_col_2]
                    if col:
                        hex.neighbors[3] = self.board[row + 1][target_col_3]
                
    def set_vertices(self):
        # This is called when the board is initialized
        # It will create all the vertices and add them to the relevant Hexes
        Vertex.init_all_vertices()
        for vertex in Vertex.vertices:
            lower = vertex.row > 5
            if vertex.row % 2 == 0: 
                # vertices on even rows have hexes to the upper left, upper right, and below
                up_left = (vertex.row // 2, vertex.col)
                up_right = (vertex.row // 2, vertex.col + 1)
                down = (vertex.row // 2 + 1, vertex.col) if lower else (vertex.row // 2 + 1, vertex.col + 1)

                # each vertex belongs to 3 different hexes
                self.board[up_left[0]][up_left[1]].vertices[2] = vertex
                self.board[up_right[0]][up_right[1]].vertices[4] = vertex
                self.board[down[0]][down[1]].vertices[0] = vertex
            else:  
                # odd row vertices have hexes above, below to the left and right
                up = (vertex.row // 2, vertex.col + 1) if lower else (vertex.row // 2, vertex.col)
                down_left = (vertex.row // 2 + 1, vertex.col)
                down_right = (vertex.row // 2 + 1, vertex.col + 1)

                # each vertex belongs to 3 different hexes
                self.board[up[0]][up[1]].vertices[3] = vertex
                self.board[down_left[0]][down_left[1]].vertices[1] = vertex
                self.board[down_right[0]][down_right[1]].vertices[5] = vertex

    def set_edges(self):
        Edge.init_all_edges()
        for hex in Hex.hexes:
            hex.edges = Edge.structured_edges[hex.row][hex.col]
    
    def __str__(self):
        string = "\n"
        for i in range(len(self.board)):
            row = str(self.board[i])
            left_margin = (3 - i) * 6 if i <=3 else (i - 3) * 6
            spaces = " " * left_margin
            string += spaces + row + "\n"
        return string

