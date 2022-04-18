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

test1 = round_rectangle(
    25,
    820-15,
    25+123.5,
    25+848,
    radius=20,
    fill="#AEADAD")
test2 = round_rectangle(
    25+123.5,
    820-15,
    25+123.5+123.5,
    25+848,
    radius=20,
    fill="#AEADAD")
test3 = round_rectangle(
    25,
    750,
    25+247,
    820-15,
    radius=20,
    fill="#AEADAD")

canvas.create_text(
    148.5, 62.5,
    text = "Chat Log",
    fill = "#b7bbc5",
    font = ("RobotoRoman-ExtraBold", int(24.0)))

text_canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=243,
    bd=0,
    highlightthickness=0,
    relief="ridge")
text_canvas.place(x=27, y=100)

text_widget = Text(text_canvas, width=20, height=1, bg="#272727", fg="#b7bbc5",
                        font="RobotoRoman-ExtraBold", padx=5, pady=5, highlightthickness=0, borderwidth=0)
text_widget.place(relheight=1, relwidth=1)
text_widget.configure(cursor="arrow", state=DISABLED)

scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)

def plotDisplay(j):
    img = PhotoImage(file='images/'+str(j)+'figure.png')
    return img


def updatePlot(j):
    img = plotDisplay(j)
    canvas.itemconfig(
       plotCanvas,
       image=img)
    canvas.imgref = img


img = plotDisplay(1)
plotCanvas = canvas.create_image(1100, 450, image=img)

button = Button(window, text="Update", command=lambda: updatePlot(2))
button.place(x=0, y=0)

button2 = Button(window, text="Reverse", command=lambda: updatePlot(1))
button2.place(x=100, y=0)

window.resizable(True, True)
window.mainloop()