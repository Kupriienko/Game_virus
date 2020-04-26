from tkinter import *
import time
import random
from tkinter import messagebox as mb

t = Tk()
t.title("Game Virus")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0, bg="white")
c.pack()
t.update()

def end():
    if len(virus_list) == 7:
        mb.showinfo("loh","вам піздец!!!!!")
        return 1
    elif len(virus_list) == 0:
        mb.showinfo("kros","ти виздорові. іди єбош!!")
        return 1
class Protector:
    def __init__(self, canvas, moe):
        self.canvas = canvas
        self.id = canvas.create_image(10,10, anchor= NW,  image = moe)
        self.canvas.move(self.id, 400, 300)
        starts = [-15, 15]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def knopka(self,event):
        if event.keysym == 'Up':
            self.canvas.move(self.id, 0, -13)
        elif event.keysym == 'Down':
            self.canvas.move(self.id, 0, 13)
        elif event.keysym == 'Left':
            self.canvas.move(self.id, -13, 0)
        else:
            self.canvas.move(self.id, 13, 0)    
    def drow(self,):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = random.randint(6, 10)
        if pos [1] >= self.canvas_height - 80:
            self.y = random.randint(-10, -6)
        if pos [0] <= 0:
            self.x = random.randint(6, 10)
        if pos [0] >= self.canvas_width - 80:
            self.x = random.randint(-10, -6) 



class ball:
    def __init__(self, canvas, moe):
        self.canvas = canvas
        self.id = canvas.create_image(10,10, anchor= NW,  image = moe)
        self.canvas.move(self.id, random.randint(0, 800), random.randint(0, 100))
        starts = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = random.randint(1, 5)
        if pos [1] >= self.canvas_height - 50:
            self.y = random.randint(-5, -1)
        if pos [0] <= 0:
            self.x = random.randint(1, 5)
        if pos [0] >= self.canvas_width - 50:
            self.x = random.randint(-5, -1)
    def check_kontakt(self , P_x, P_y):
        pos = self.canvas.coords(self.id)
        if pos[0] > (P_x - 40.00) and pos[0] < (P_x + 40.00) and pos[1] > (P_y - 40) and pos[1] < (P_y + 40):
            return 1
        else:
            return 0
           



            
moe =(PhotoImage(file= 'ukol.png'))
Protec = Protector(c, moe)

c.bind_all('<KeyPress-Up>', Protec.knopka)
c.bind_all('<KeyPress-Down>', Protec.knopka)
c.bind_all('<KeyPress-Left>', Protec.knopka)
c.bind_all('<KeyPress-Right>', Protec.knopka)


virus_list = []
virusy = (PhotoImage(file='virus1.png'),
PhotoImage(file='virus2.png'),
PhotoImage(file='virus3.png'),
PhotoImage(file='virus4.png'))
virus_list.append(ball(c, virusy[random.randint(0,3)]))

h = time.time()
while 1:
    #b.drow()
    b_pos = c.coords(Protec.id)
    i = 0
    for x in virus_list:
        if x.check_kontakt(b_pos[0],b_pos[1]) == 1: 
            c.delete(virus_list.pop(i).id)
        else:
            x.draw()
            i = i + 1
    if time.time() - h >= 3.000:
        virus_list.append(ball(c, virusy[random.randint(0,3)]))
        h = time.time()
    if end() == 1:
        break
    t.update_idletasks()
    t.update()
    time.sleep(0.01)
    
        
