import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

color = 0

def draw(canvas):

    if color == 0:
        canvas.draw_circle([150, 80], 30, 2, "white", "red")
        canvas.draw_circle([150, 160], 30, 2, "white", "black")
        canvas.draw_circle([150, 240], 30, 2, "white", "black")
    elif color == 1:
        canvas.draw_circle([150, 80], 30, 2, "white", "black")
        canvas.draw_circle([150, 160], 30, 2, "white", "yellow")
        canvas.draw_circle([150, 240], 30, 2, "white", "black")
    else:
        canvas.draw_circle([150, 80], 30, 2, "white", "black")
        canvas.draw_circle([150, 160], 30, 2, "white", "black")
        canvas.draw_circle([150, 240], 30, 2, "white", "green")

def timer():
    global color

    if color == 0:
        color = 1
    elif color == 1:
        color = 2
    else:
        color = 0

timer = simplegui.create_timer(1000, timer)
frame = simplegui.create_frame("super svetofor", 300, 300)

frame.set_draw_handler(draw)

timer.start()
frame.start()
