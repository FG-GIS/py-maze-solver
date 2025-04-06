from graphics import Window, Point, Line, Cell
from maze import Maze

def main():
    win = Window(800,600)
    # line_1 = Line(Point(100,100),Point(100,500))
    # line_2 = Line(Point(100,100),Point(700,100))
    # win.draw_line(line_1,"black")
    # win.draw_line(line_2,"black")
    # testing cells
    # full cell
    c1 = Cell(Point(380,100),Point(400,120),win, b_wall=False)
    # no left wall
    c2 = Cell(Point(380,120),Point(400,140),win,t_wall=False)
    # no right wall
    # c3 = Cell(Point(380,140),Point(400,160),win,r_wall=False)
    # no top wall
    # c4 = Cell(Point(380,160),Point(400,180),win,t_wall=False)

    # num_rows = 5
    # num_cols = 10
    # margin = 50
    # cell_width = 20
    # cell_height = 20
    # gap = 10

    # for row in range(num_rows):
    #     for col in range(num_cols):
    #         x1 = margin + col * (cell_width + gap)
    #         y1 = margin + row * (cell_height + gap)
    #         x2 = x1 + cell_width
    #         y2 = y1 + cell_height

    #         # For the first row, draw cells with all walls.
    #         if row == 0:
    #             cell = Cell(Point(x1, y1), Point(x2, y2), win)
    #         # For subsequent rows, remove one wall per row:
    #         elif row == 1:
    #             cell = Cell(Point(x1, y1), Point(x2, y2), win, l_wall=False)
    #         elif row == 2:
    #             cell = Cell(Point(x1, y1), Point(x2, y2), win, r_wall=False)
    #         elif row == 3:
    #             cell = Cell(Point(x1, y1), Point(x2, y2), win, t_wall=False)
    #         elif row == 4:
    #             cell = Cell(Point(x1, y1), Point(x2, y2), win, b_wall=False)
    #         cell.draw()

    c1.draw()
    c2.draw()
    c1.draw_move(c2)
    # c3.draw()
    # c4.draw()

    m1 = Maze(200,200,40,40,10,10,win)

    win.wait_for_close()

main()