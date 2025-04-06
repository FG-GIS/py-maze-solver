from graphics import Point, Cell, Window
from time import sleep

class Maze():
    def __init__(self, x: int, y: int,
                 num_rows: int, num_cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Window):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._cells = None
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
                if i == 0:
                    l_w = True
                else:
                    l_w = False
                
                if i == self.num_cols - 1:
                    r_w = True
                else:
                    r_w = False
                
                if j == 0:
                    t_w = True
                else:
                    t_w = False
                
                if j == self.num_rows - 1:
                    b_w = True
                else:
                    b_w = False

                n_cell = Cell(Point(col_x1, row_y1), Point(col_x2, row_y2), self._win,l_wall= l_w, 
                              r_wall= r_w, t_wall= t_w, b_wall= b_w)
                self._cells[i].append(n_cell)
        self._draw_cells()

    def _draw_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].draw()
                self._animate()
    
    def _animate(self):
        self._win.redraw()
        sleep(.05)