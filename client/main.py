from tkinter import *
from move import *
from objects import Objects
import time
import threading

root = Tk()
canv = Canvas(root, width=500, height=500, bg='black')
canv.pack()

movement_vector = Vector()
movement_speed = 5
mass = 10

eve = Vector(10, 10)
def res(event):
    global eve
    eve = Vector(event.x, event.y)


obj = Move(Vector(10, 10))
o = Objects(size=10, grad=25, cords=(obj.x, obj.y))
def motion():
    global eve
    while True:
        moment_vector = obj.sb_arrive(eve.x, eve.y)
        o.draw(canv, (moment_vector.x, moment_vector.y))
        canv.update()
        time.sleep(0.01)


th = threading.Thread(target=motion)
th.start()
root.bind("<Motion>", res)
root.mainloop()
