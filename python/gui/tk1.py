#!/usr/bin/env python

from Tkinter import Tk, Frame, Canvas
import ImageTk

t = Tk()
t.title("Trans")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="test.png")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()
