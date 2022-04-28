from tkinter import *
from VA import RASA
import Logging
import os
from Plots import plotting
import glob
import time
from datetime import datetime, timezone

from foldercreation import folder
#on the second day God created time by importing
if __name__ == "__main__":
    folder.Create()
    plotting.linePlot("Dates", "DNT (Mean)", "Country", "Hospital", plotting.df, folder.baseFolder)
    RASA = RASA()
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


    def _on_enter_pressed(event):
        msg = msg_entry.get()
        _insert_message(msg, "You")


    def _talk_to_va(event):
        msg = RASA.VArecord()
        msg_entry.delete(0, END)
        msg1 = f"You: {msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)


        va_msg = RASA.VAnlu(msg)
        text_widget.configure(state=NORMAL)
        for va in va_msg:
            msg2 = f"Assistant: {va}\n\n"
            text_widget.insert(END, msg2)
            RASA.VAspeak(va)
            Logging.reply_logger.append(msg2)  # logging
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        updatePlot(newestFigure()) #updates the dashboard aUtOmAtIcLy
        Logging.reply_logger.append(msg1)  # logging
        #Logging.reply_logger.append(msg2)  # logging


    def _insert_message(msg, sender):
        if not msg:
            return
        msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        _insert_va_message(msg1)
        updatePlot(newestFigure())  # updates the dashboard aUtOmAtIcLy
        Logging.reply_logger.append(msg1)  # logging


    def _insert_va_message(msg):
        va_msg = RASA.VAnlu(msg)
        text_widget.configure(state=NORMAL)
        for va in va_msg:
            msg2 = f"Assistant: {va}\n\n"
            text_widget.insert(END, msg2)
            RASA.VAspeak(va)
            Logging.reply_logger.append(msg2)  # logging
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        updatePlot(newestFigure())  # updates the dashboard aUtOmAtIcLy


    def btn_clicked():
        print("Button Clicked")

    window = Tk()

    window.geometry("1699x900")
    window.configure(bg="#DEE4E7")
    canvas = Canvas(
        window,
        bg="#DEE4E7",
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    canvas.pack()
    RoundRectangleborder = round_rectangle(
        23,
        23,
        25 + 247 + 2,
        25 + 848 + 2,
        radius=20,
        fill="#000000")
    RoundRectangle = round_rectangle(
        25,
        25,
        25 + 247,
        25 + 848,
        radius=20,
        fill="#FFFFFF")

    ##############################################This code creates the button to send written messages
    send_box = round_rectangle(
        25,
        820 - 15,
        25 + 123.5,
        25 + 848,
        radius=20,
        fill="#ECEFF1")
    send_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=68,
        width=118.5,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    send_canvas.place(x=25 + 5, y=805)
    send_button = Button(send_canvas, text="Send", font="RobotoRoman-ExtraBold", borderwidth=0,
                         bg="#ECEFF1", command=lambda: _on_enter_pressed(None))
    send_button.place(x=0, y=0, relheight=1, relwidth=1)
    ##############################################

    ##############################################This code creates a button for talking to VA
    record_box = round_rectangle(
        25 + 123.5,
        820 - 15,
        25 + 123.5 + 123.5,
        25 + 848,
        radius=20,
        fill="#ECEFF1")
    record_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=68,
        width=118.5,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    record_canvas.place(x=25 + 123.5, y=805)
    record_button = Button(record_canvas, text="Talk", font="RobotoRoman-ExtraBold", borderwidth=0,
                           bg="#ECEFF1", command=lambda: _talk_to_va(None))
    record_button.place(x=0, y=0, relheight=1, relwidth=1)

    record_line = Label(record_canvas, width=450, bg="#000000")
    record_line.place(relwidth=0.012, relx=0.01, relheight=1)
    ##############################################

    ##############################################This code creates the text box for users to write messages in
    msg_entry_box = round_rectangle(
        25,
        750,
        25 + 247,
        820,
        radius=20,
        fill="#ECEFF1")
    msg_entry_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=55,
        width=237,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    msg_entry_canvas.place(x=25 + 5, y=750)
    msg_entry = Entry(msg_entry_canvas, bg="#ECEFF1", fg="#000000", borderwidth=0, font="RobotoRoman-ExtraBold")
    msg_entry.place(relwidth=1, relheight=1, rely=0.008, relx=0.011)
    msg_entry.focus()

    entry_line = Label(msg_entry_canvas, width=450, bg="#000000")
    entry_line.place(relwidth=1, rely=0.99, relheight=0.012)
    ##############################################

    ##############################################This code creates the chat log.
    canvas.create_text(
        148.5, 62.5,
        text="Chat Log",
        fill="#b7bbc5",
        font=("RobotoRoman-ExtraBold", int(24.0)))

    text_canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=650,
        width=243,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    text_canvas.place(x=27, y=100)

    text_widget = Text(text_canvas, width=20, height=1, bg="#FFFFFF", fg="#b7bbc5",
                       font="RobotoRoman-ExtraBold", padx=5, pady=5, highlightthickness=0, borderwidth=0)
    text_widget.place(relheight=1, relwidth=0.95)
    text_widget.configure(cursor="arrow", state=DISABLED)

    scrollbar = Scrollbar(text_canvas)
    scrollbar.place(relheight=1, relx=0.95)
    scrollbar.configure(command=text_widget.yview)
    ##############################################

    def plotDisplay(filename):
        img = PhotoImage(file=filename, master=window)
        print(img)
        return img


    def updatePlot(filename):
        img = plotDisplay(filename)
        canvas.itemconfig(
           plotCanvas,
           image=img)
        canvas.imgref = img

    def newestFigure():
        list_of_files = glob.glob('logs/images/*')  # * means all if need specific format then *.csv
        print(list_of_files)
        return max(list_of_files, key=os.path.getctime)

#    def clock():
#        time = datetime.now().strftime("Time: %H:%M:%S")
#        # lab['text'] = time
#        #if img == newestFigure()
#        updatePlot(newestFigure())
#        window.after(1000, clock)  # run itself again after 1000 ms

    img = plotDisplay(newestFigure())
    imageoutline = round_rectangle(
        400 - 3,
        25 - 3,
        1875 + 3,
        25 + 848 + 3,
        radius=20,
        fill="#000000")
    imageborder = round_rectangle(
        400,
        25,
        1875,
        25 + 848,
        radius=20,
        fill="#FFFFFF")
    plotCanvas = canvas.create_image(1100, 450, image=img)

    button = Button(window, text="Update", command=lambda: updatePlot(newestFigure()))
    button.place(x=0, y=0)

    button2 = Button(window, text="Reverse", command=lambda: updatePlot(1))
    button2.place(x=100, y=0)

    # button3 = Button(window, text="RASA", command=lambda: RASA.VAIntro())
    # button3.place(x=200, y=0)
    #
    # button4 = Button(window, text="RASA", command=lambda: _talk_to_va(None))
    # button4.place(x=300, y=0)

    ####################    On exit #################################################################
    def on_closing():
        print('close')
        Logging.logToCSV()
        folder.RenameLogFolder()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.resizable(True, True)
    window.mainloop()