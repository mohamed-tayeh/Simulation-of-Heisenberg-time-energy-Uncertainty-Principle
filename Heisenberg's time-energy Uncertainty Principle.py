from tkinter import *
import random
import time

tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=600, bd=0, bg='black', highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.m = random.randint(15,101)
        self.n = random.randint(15,101)
        self.radius = ((self.n - self.m)**2 * 2) ** 0.5
        self.id = canvas.create_oval(self.m, self.m, self.n, self.n, fill=color)
        x_start = random.randint(5, 596)
        y_start = random.randint(5, 596)
        self.canvas.move(self.id, x_start, y_start)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

colours = ['magenta', 'magenta', 'red', 'magenta','blue', 'blue', 'orange', 'yellow', 'green']

def random_colours():
    random.shuffle(colours)

colour = colours[0]
ball = Ball(canvas, colour)
c = 0

while True:
    c += 0.01
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if c >= 1/(ball.radius/30):
        c = 0
        random_colours()
        colour = colours[0]
        canvas.delete(ball.id)
        ball = Ball(canvas, colour)