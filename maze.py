from graphics import Point, Cell, Window
from time import sleep
import random

class Maze():
    def __init__(self, x: int, y: int,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Window= None, seed: int = None):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col_x1 = self.x + (i * self.cell_size_x)
            col_x2 = col_x1 + self.cell_size_x
            self._cells.append([])
            for j in range(self.num_rows):
                row_y1 = self.y + (j * self.cell_size_y)
                row_y2 = row_y1 + self.cell_size_y
                n_cell = Cell(Point(col_x1, row_y1), Point(col_x2, row_y2), self._win)
                self._cells[i].append(n_cell)
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _draw_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if self._win is None:
                    return
                self._cells[i][j].draw()
                self._animate(.02)
    
    def _draw_cell(self, i: int, j: int):
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate(.02)
    
    def _animate(self, t: float):
        if self._win is None:
            return
        self._win.redraw()
        sleep(t)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_wall(self, i: int,j: int,wall: str):
        match wall:
                case "l":
                    self._cells[i][j].has_left_wall = False
                case "t":
                    self._cells[i][j].has_top_wall = False
                case "r":
                    self._cells[i][j].has_right_wall = False
                case "b":
                    self._cells[i][j].has_bottom_wall = False

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            # check left neighbour-cell
            if i-1 > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j,("l","r")))
            # check top neighbour-cell
            if j-1 > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1,("t","b")))
            # check right neighbour-cell
            if i+1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j,("r","l")))
            # check bottom neighbour-cell
            if j+1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1,("b","t")))
            
            # check possible directions
            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            
            n_i,n_j,walls = to_visit[random.randrange(len(to_visit))]

            self._break_wall(i,j,walls[0])
            self._break_wall(n_i,n_j,walls[1])
            self._break_walls_r(n_i,n_j)
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self,i: int = 0,j: int = 0) -> bool:
        self._animate(.07)
        self._cells[i][j].visited = True

        if i == self.num_cols-1 and j == self.num_rows - 1:
            return True
        
        # check left-neighbour-cell
        if i-1 > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)
        # check top-neighbour-cell
        if j-1 > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)
        # check right-neighbour-cell
        if i+1 < self.num_cols and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)
        # check bottom-neighbour-cell
        if j+1 < self.num_rows and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)
        
        return False



    def solve(self) -> bool:
        return self._solve_r()

