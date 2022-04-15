from tkinter import *

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1699x900")
window.configure(bg = "#121212")
canvas = Canvas(
    window,
    bg = "#121212",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.pack()
RoundRectangle = round_rectangle(
    25,
    25,
    25+247,
    25+848,
    radius=20,
    fill="#272727")

canvas.create_text(
    148.5, 62.5,
    text = "HISTORY",
    fill = "#b7bbc5",
    font = ("RobotoRoman-ExtraBold", int(24.0)))


def plotDisplay(j):
    img = PhotoImage(file='images/'+str(j)+'figure.png')
    return img


img = plotDisplay(1)
canvas.create_image(1100, 450, image=img)

window.resizable(True, True)
window.mainloop()
