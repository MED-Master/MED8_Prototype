from tkinter import *



def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1699x900")
window.configure(bg = "#a7a5a9")
canvas = Canvas(
    window,
    bg = "#a7a5a9",
    height = 900,
    width = 1699,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


HeaderShadow = canvas.create_rectangle(
    10, 10, 10+1684, 10+47,
    fill = "#666666",
    outline = "")


MainShadow = canvas.create_rectangle(
    261, 69, 261+1433, 69+824,
    fill = "#666666",
    outline = "")


MenuShadow = canvas.create_rectangle(
    10, 69, 10+245, 69+824,
    fill = "#666666",
    outline = "")


Header = canvas.create_rectangle(
    10, 7, 10+1682, 7+48,
    fill = "#e57bee",
    outline = "")


Menu = canvas.create_rectangle(
    10, 66, 10+243, 66+825,
    fill = "#818181",
    outline = "")


MainPlot = canvas.create_rectangle(
    261, 66, 261+1431, 66+825,
    fill = "#e3e1e1",
    outline = "")

DashboardName = canvas.create_text(
    135.0, 27.5,
    text = "Dashboard",
    fill = "#eee9e9",
    font = ("RobotoRoman-Regular", int(36.0)))

print(MainShadow)

window.resizable(False, False)
window.mainloop()
