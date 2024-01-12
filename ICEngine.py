import turtle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser
import pygame
import time
import os
import sys

pygame.mixer.init()  # initialise the pygame


def play():
    pygame.mixer.music.load(resource_path0("drawing_music.mp3"))
    pygame.mixer.music.play(loops=0)


def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def draw_engine():
    global new_window
    try:
        new_window.focus()
    except:

        def stop_music_fun():
            pygame.mixer.music.stop()

        new_window = Toplevel(root)
        new_window.title('Internal Combustion Engine')
        new_window.geometry("800x600")
        # new_window.iconbitmap('icon.ico')
        new_window.configure(bg='#E6E6E6')
        # new_window.create_image(450, 150, image=bg, anchor="center", )
        new_window.resizable(width=False, height=False)

        def on_closing_new_window():
            if pygame.mixer.music.get_busy():
                # Stop audio playback before closing the application
                pygame.mixer.music.stop()
            new_window.destroy()

        new_window.protocol("WM_DELETE_WINDOW",
                            on_closing_new_window)

        new_window.after(1000*25, stop_music_fun)
        windowWidth = new_window.winfo_reqwidth()
        windowHeight = new_window.winfo_reqheight()
        new_window.geometry("+{}+{}".format(int(root.winfo_screenwidth() / 3.15 - windowWidth / 2),
                                            int(root.winfo_screenheight() / 3.85 - windowHeight / 2)))

        # creating canvas
        canvas = Canvas(new_window, width=800, height=300,  highlightthickness=0,
                        highlightbackground="#c0c0c0")
        turtle_screen = turtle.TurtleScreen(canvas)
        turtle_screen.bgcolor("#fdefe2")

        # creating label for heading
        icEngineHeading = Label(new_window, text='\u2699 INTERNAL COMBUSTION ENGINE SKETCH', font=(
            'Arial', 18, 'bold', 'underline'), bg="#fdefe2", fg='#725c52', padx=10)
        icEngineHeading.place(x=140, y=15)

        # Drawing the IC Engine using turtle
        canvas.pack(fill="both", expand=True)
        pencil = turtle.RawTurtle(turtle_screen)

        # start playing drawing music
        play()

        # pencil.shape("turtle")
        pencil.speed(2)
        pencil.width(3)

        # Move the turtle to the starting position
        pencil.penup()
        pencil.goto(-100, -400)
        pencil.pendown()

        # Draw ICE Engine in turtle
        pencil.color("#715548")
        pencil.forward(200)
        pencil.left(90)
        pencil.forward(200)
        pencil.goto(50, -150)
        pencil.penup()
        pencil.goto(-100, -400)
        pencil.pendown()
        pencil.forward(200)
        pencil.goto(-50, -150)
        pencil.forward(150)
        pencil.penup()
        pencil.goto(50, -150)
        pencil.pendown()
        pencil.forward(150)
        pencil.penup()
        pencil.goto(30, -10)
        pencil.pendown()
        pencil.forward(20)
        pencil.penup()
        pencil.goto(20, -10)
        pencil.pendown()
        pencil.forward(20)
        pencil.penup()
        pencil.goto(-30, -10)
        pencil.pendown()
        pencil.forward(20)
        pencil.penup()
        pencil.goto(-20, -10)
        pencil.pendown()
        pencil.forward(20)
        pencil.penup()
        pencil.goto(-50, 0)
        pencil.pendown()
        pencil.right(90)
        pencil.forward(20)
        pencil.penup()
        pencil.forward(10)
        pencil.pendown()
        pencil.forward(40)
        pencil.penup()
        pencil.forward(10)
        pencil.pendown()
        pencil.forward(20)

        pencil.penup()
        pencil.goto(0, -350)
        pencil.pendown()
        pencil.circle(60)
        pencil.penup()
        pencil.goto(0, -310)
        pencil.pendown()
        pencil.circle(20)
        pencil.penup()
        pencil.goto(20, -285)
        pencil.pendown()
        pencil.left(55)
        pencil.forward(80)
        pencil.penup()
        pencil.goto(0, -270)
        pencil.pendown()
        pencil.forward(80)
        pencil.right(145)
        pencil.circle(15)
        pencil.right(150)
        pencil.forward(100)
        pencil.penup()
        pencil.backward(100)
        pencil.left(25)
        pencil.backward(20)
        pencil.right(90)
        pencil.forward(20)
        pencil.left(70)
        pencil.pendown()
        pencil.forward(115)
        pencil.circle(10)

        # making smaller circles
        pencil.penup()
        pencil.forward(5)
        pencil.left(90)
        pencil.forward(10)
        pencil.pendown()
        pencil.circle(3.5)
        pencil.penup()
        pencil.right(90)

        pencil.penup()
        pencil.goto(-5, -295)
        pencil.pendown()
        pencil.circle(-7)
        pencil.penup()
        # ________________

        pencil.goto(-50, -95)
        pencil.left(55)
        pencil.pendown()
        pencil.backward(100)
        pencil.goto(50, -100)
        pencil.forward(100)
        pencil.goto(-50, -120)
        pencil.backward(50)
        pencil.penup()
        pencil.backward(20)
        pencil.pendown()
        pencil.backward(30)
        pencil.goto(50, -125)
        pencil.forward(30)
        pencil.penup()
        pencil.forward(20)
        pencil.pendown()
        pencil.forward(50)
        pencil.backward(5)
        pencil.left(90)
        pencil.forward(25)
        pencil.backward(25)
        pencil.penup()
        pencil.backward(5)
        pencil.pendown()
        pencil.backward(20)
        pencil.penup()
        pencil.backward(5)
        pencil.pendown()
        pencil.backward(25)
        pencil.left(90)
        pencil.forward(90)
        pencil.right(90)
        pencil.forward(25)
        pencil.penup()
        pencil.forward(5)
        pencil.pendown()
        pencil.forward(20)
        pencil.penup()
        pencil.forward(5)
        pencil.pendown()
        pencil.forward(25)
        pencil.right(90)
        pencil.forward(5)
        pencil.penup()
        pencil.forward(25)
        pencil.pendown()
        pencil.forward(60)
        # __________________

        # making the valve closers
        pencil.penup()
        pencil.goto(-27, 25)
        pencil.pendown()
        pencil.left(90)
        pencil.pendown()
        pencil.forward(50)
        pencil.right(90)
        pencil.forward(7)
        pencil.left(90)
        pencil.forward(3)
        pencil.left(90)
        pencil.forward(18)
        pencil.left(90)
        pencil.forward(3)
        pencil.left(90)
        pencil.forward(7)
        pencil.right(90)
        pencil.forward(50)

        pencil.penup()
        pencil.right(180)
        pencil.goto(23, 25)
        pencil.pendown()
        pencil.forward(50)
        pencil.right(90)
        pencil.forward(7)
        pencil.left(90)
        pencil.forward(3)
        pencil.left(90)
        pencil.forward(18)
        pencil.left(90)
        pencil.forward(3)
        pencil.left(90)
        pencil.forward(7)
        pencil.right(90)
        pencil.forward(50)
        # ____________________

        # making the spark plug
        pencil.penup()
        pencil.goto(-5, 0)
        pencil.pendown()
        pencil.forward(25)
        pencil.circle(-5, 180)
        pencil.forward(25)
        # ____________________

        def label_engine():

            exhaust_valve = Label(canvas, text='Exhaust Valve', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            exhaust_valve.place(x=600, y=120)
            canvas.create_line(30, -13, 180, -15, arrow=LAST)

            cylinder = Label(canvas, text='Cylinder', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            cylinder.place(x=600, y=170)
            canvas.create_line(40, 50, 180, 30, arrow=LAST)

            piston_rings = Label(canvas, text='Piston Rings', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            piston_rings.place(x=600, y=220)
            canvas.create_line(45, 100, 180, 80, arrow=LAST)
            canvas.create_line(45, 125, 180, 80, arrow=LAST)

            piston = Label(canvas, text='Piston', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            piston.place(x=600, y=270)
            canvas.create_line(40, 140, 180, 130, arrow=LAST)

            connecting_rod = Label(canvas, text='Connecting Rod', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            connecting_rod.place(x=600, y=320)
            canvas.create_line(40, 180, 180, 180, arrow=LAST)

            crank = Label(canvas, text='Crank', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            crank.place(x=600, y=370)
            canvas.create_line(40, 230, 180, 230, arrow=LAST)

            crank_shaft = Label(canvas, text='Crank Shaft', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            crank_shaft.place(x=150, y=370)
            canvas.create_line(0, 300, -170, 230, arrow=LAST)

            crank_case = Label(canvas, text='Crank Case', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            crank_case.place(x=150, y=320)
            canvas.create_line(-90, 220, -175, 180, arrow=LAST)

            inlet_valve = Label(canvas, text='Inlet Valve', font=(
                'Consolas', 8, 'bold',), bg='#ebd0bf', padx=5)
            inlet_valve.place(x=150, y=120)
            canvas.create_line(-30, -13, -180, -15, arrow=LAST)

            label_button.place_forget()

        label_button = Button(new_window, bg='#715548', text="Label Diagram", font=(
            'Consolas', 14, 'bold'), fg='white', bd=2, padx=10, relief='groove', command=label_engine)
        label_button.place(x=315, y=60)


def open_youtube_link():
    if messagebox.askokcancel('Confirmation Box', 'This will lead to an external youtube link?', parent=root):
        webbrowser.open("https://youtu.be/Y32gDgLq6hE?si=cThlyOR_Nq0BUnK7")
    else:
        pass


# _____ ROOT WINDOW OF THE TKINTER APP _____
# Creating the main Tkinter window
root = Tk()
root.title('Mechanical Engineering AAT 2')
root.resizable(width=False, height=False)
# root.iconbitmap('icon.ico')
root.geometry("900x700")
rootWidth = root.winfo_reqwidth()
rootHeight = root.winfo_reqheight()
root.geometry("+{}+{}".format(int(root.winfo_screenwidth() / 3.5 - rootWidth / 2),
                              int(root.winfo_screenheight() / 5 - rootHeight / 2)))

# root.wm_attributes('-transparentcolor', root['bg'])

# Creating a canvas window to present the app
backgroundImage = (Image.open(resource_path0('backgroundJpgImage.jpg')))
backgroundImage = backgroundImage.resize(
    (900, 700), Image.Resampling.LANCZOS)
backgroundImage = ImageTk.PhotoImage(backgroundImage)

canvas = Canvas(root, width=900, height=700, bg='white')
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=NW, image=backgroundImage)
preHeading = Label(canvas, text='COURSE PROJECT: AAT-2', font=(
    'Consolas', 16, 'bold'), bg='#ebd0bf', padx=10)
preHeading.place(x=120, y=150)
heading = Label(canvas, text='DEPARTMENT OF MECHANICAL ENGINEERING', font=(
    'Consolas', 22, 'bold', 'underline'), bg='#fdefe2', padx=10)
heading.place(x=150, y=240)
subHeading1 = Label(canvas, text='COURSE NAME   : Intoduction to Mechanical Engineering', font=(
    'Consolas', 14, 'bold'), bg='#fdefe2', padx=10)
subHeading1.place(x=85, y=300)
subHeading2 = Label(canvas, text='COURSE CODE   : BESCK104D', font=(
    'Consolas', 14, 'bold'), bg='#fdefe2', padx=10)
subHeading2.place(x=85, y=330)
subHeading3 = Label(canvas, text='PROJECT TITLE : Internal Combustion Engine', font=(
    'Consolas', 14, 'bold'), bg='#fdefe2', padx=10)
subHeading3.place(x=85, y=360)
heading2 = Label(canvas, text='Coded and presented by', font=(
    'Consolas', 20, 'bold', 'underline'), bg='#fdefe2', padx=10)
heading2.place(x=85, y=400)
nameLabel1 = Label(canvas, text='\u2022 Anurag Rai,    Roll no: --', font=(
    'Consolas', 14, 'bold',), bg='#fdefe2', padx=10)
nameLabel1.place(x=85, y=450)


# Create a button to draw Internal Combustion Engine
draw_button = Button(root, bg='#715548', text="Draw IC Engine \u270E", font=(
    'Consolas', 16, 'bold'), fg='white', bd=2, padx=20, relief='groove', command=draw_engine)
draw_button.place(x=100, y=530)

learn_button = Button(root, bg='#715548', text="Learn its working", font=(
    'Consolas', 16, 'bold'), fg='white', bd=2, padx=20, relief='groove', command=open_youtube_link)
learn_button.place(x=400, y=530)


# Run the Tkinter event loop
root.mainloop()
# _____ ROOT WINDOWS ENDS HERE _____
