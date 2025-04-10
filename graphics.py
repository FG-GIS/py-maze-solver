from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, cnv: Canvas, fill_color: str):
        cnv.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y, fill=fill_color, width=2)


class Window():
    def __init__(self, width: int = 400, height: int = 400):
        self.__root = Tk()
        self.__root.title("Test TKinter")

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__runningFlag = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__runningFlag = True
        while self.__runningFlag:
            self.redraw()
        print("window closed")
    
    def close(self):
        self.__runningFlag = False
    
    def draw_line(self, l: Line, fill_color: str):
        l.draw(self.__canvas,fill_color)


class Cell():
    def __init__(self, top_left_point: Point,bottom_right_point: Point, window: Window = None,
                 l_wall = True, r_wall = True, t_wall = True, b_wall = True):
        self.__x1 = top_left_point.x
        self.__y1 = top_left_point.y
        self.__x2 = bottom_right_point.x
        self.__y2 = bottom_right_point.y
        self.__win = window
        self.has_left_wall = l_wall
        self.has_right_wall = r_wall
        self.has_top_wall = t_wall
        self.has_bottom_wall = b_wall
        self.visited = False
    
    def draw(self):
        if self.__win is None:
            return
        tl_p = Point(self.__x1,self.__y1)
        tr_p = Point(self.__x2,self.__y1)
        bl_p = Point(self.__x1,self.__y2)
        br_p = Point(self.__x2,self.__y2)

        # Left Wall
        l = Line(tl_p,bl_p)
        cl = "white"
        if self.has_left_wall:
            cl = "black"
        self.__win.draw_line(l,cl)

        # Right Wall
        l = Line(tr_p,br_p)
        cl = "white"
        if self.has_right_wall:
            cl = "black"
        self.__win.draw_line(l,cl)

        # Top wall
        l = Line(tl_p,tr_p)
        cl = "white"
        if self.has_top_wall:
            cl = "black"
        self.__win.draw_line(l,cl)

        # Bottom Wall
        l = Line(bl_p,br_p)
        cl = "white"
        if self.has_bottom_wall:
            cl = "black"
        self.__win.draw_line(l,cl)
    
    def draw_move(self, to_cell: 'Cell', undo = False):
        self_center = Point((self.__x2-self.__x1)//2+self.__x1,(self.__y2-self.__y1)//2+self.__y1)
        c_center = Point((to_cell.__x2-to_cell.__x1)//2+to_cell.__x1,(to_cell.__y2-to_cell.__y1)//2+to_cell.__y1)

        color = "red"
        if undo:
            color = "grey"

        if self.__win is None:
            return
        self.__win.draw_line(Line(self_center,c_center),color)

