from tkinter import *

from VA import RASA
from Logging import Logger
import os
from Plots import plotting
import glob
import threading
import numpy as np
from Figure import figure


from foldercreation import folder
#on the second day God created time by importing
if __name__ == "__main__":
    folder.Create()
    plotting.dnt_barplot_bycountry("Country", "DNT (Median)", plotting.df, folder.baseFolder, "Comparing mean DNT internationally (2022 Q1)")
    RASA = RASA()
    figure = figure()
    LogObject = Logger()
    LogObject.startEnd_logger.append(LogObject.dateTime())
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


    def _on_enter_pressed(event): #When you press the send button
        msg = msg_entry.get()
        _enter_user_message(msg, "You")
        LogObject.button_logger.append('send')
        LogObject.timerButton_logger.append(LogObject.dateTime())


    def _talk_to_va(event): #When you press the talk button
        msg = RASA.VArecord()
        msg_entry.delete(0, END)
        msg1 = f"You: {msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)
        LogObject.reply_logger.append(msg1)  # logging
        LogObject.button_logger.append('talk')
        LogObject.timerButton_logger.append(LogObject.dateTime())


        va_msg = RASA.VAnlu(msg)
        text_widget.configure(state=NORMAL)
        t = threading.Thread(target=_read_out_VA_message, args=[va_msg])
        t.start()
        _reply_to_text_widget(va_msg)
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        updatePlot(figure.newestFigure()) # updates the dashboard aUtOmAtIcLy




    def _enter_user_message(msg, sender): #prints the message inside the text_widget
        if not msg:
            return
        msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        LogObject.reply_logger.append(msg1)  # logging
        _insert_va_message(msg)
        


    def _insert_va_message(msg): #prints the VA's message inside the text_widget
        va_msg = RASA.VAnlu(msg)
        text_widget.configure(state=NORMAL)
        t = threading.Thread(target=_read_out_VA_message, args=[va_msg])
        t.start()
        end_trigger = _reply_to_text_widget(va_msg)
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        updatePlot(figure.newestFigure())  # updates the dashboard aUtOmAtIcLy
        if end_trigger:
            LogObject.logToCSV()

    def _read_out_VA_message(va_msg):
        for va in va_msg:
            RASA.VAspeak(va)

    def _reply_to_text_widget(va_msg):
        for va in va_msg:
            if va == "Thanks for the discussion, looking forward to the next session!":
                end_trigger = True
            else:
                end_trigger = False
            msg2 = f"Assistant: {va}\n\n"
            text_widget.insert(END, msg2)
            LogObject.reply_logger.append(msg2)  # logging
        return end_trigger

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
        25 + 247 + 2 + 100,
        25 + 848 + 2,
        radius=20,
        fill="#000000")
    RoundRectangle = round_rectangle(
        25,
        25,
        25 + 247 + 100,
        25 + 848,
        radius=20,
        fill="#FFFFFF")

    ##############################################This code creates the button to send written messages
    send_box = round_rectangle(
        25,
        820 - 15,
        25 + 123.5 + 50,
        25 + 848,
        radius=20,
        fill="#ECEFF1")
    send_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=68,
        width=118.5 + 50,
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
        25 + 123.5 + 50,
        820 - 15,
        25 + 123.5 + 123.5 + 50,
        25 + 848,
        radius=20,
        fill="#ECEFF1")
    record_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=68,
        width=118.5 + 50,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    record_canvas.place(x=25 + 123.5 + 50, y=805)
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
        25 + 247 + 100,
        820,
        radius=20,
        fill="#ECEFF1")
    msg_entry_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=55,
        width=237 + 100,
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
        148.5 + 50,
        62.5,
        text="Chat Log",
        fill="#b7bbc5",
        font=("RobotoRoman-ExtraBold", int(24.0)))

    text_canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=650,
        width=243 + 100,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    text_canvas.place(x=27, y=100)

    text_widget = Text(text_canvas, width=20 + 100, height=1, bg="#FFFFFF", fg="#000000",
                       font="RobotoRoman-ExtraBold", padx=5, pady=5, highlightthickness=0, borderwidth=0, wrap = WORD)
    text_widget.place(relheight=1, relwidth=0.95)
    text_widget.configure(cursor="arrow", state=DISABLED)

    scrollbar = Scrollbar(text_canvas)
    scrollbar.place(relheight=1, relx=0.95)
    scrollbar.configure(command=text_widget.yview)
    ##############################################

    def firstFigure():
        list_of_files = glob.glob('logs/images/*')  # * means all if need specific format then *.csv
        return max(list_of_files, key=os.path.getctime)

    def plotDisplay(filename):
        img = PhotoImage(file=filename, master=window)
        return img

    def updatePlot(filename):
        img = plotDisplay(filename)
        canvas.itemconfig(
           plotCanvas,
           image=img)
        canvas.imgref = img

    img = plotDisplay(firstFigure())

    #print('current plot', CurrentPlot())


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

    plotCanvas = canvas.create_image(1150, 425, image=img)

# #####################################################THIS code draws the box for the forward/backwards buttons
    image_movement_box_border = round_rectangle(
        825-3,
        890-3,
        1400+3,
        990+3,
        radius=20,
        fill="#000000")
    image_movement_box = round_rectangle(
        825,
        890,
        1400,
        990,
        radius=20,
        fill="#FFFFFF")
    image_movement_canvas = Canvas(
        window,
        bg="#ECEFF1",
        height=95,
        width=570,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    image_movement_canvas.place(x=830-2, y=895-3)
    button_line = Label(image_movement_canvas, width=450, bg="#000000")
    button_line.place(relwidth=0.001, relx=0.5, relheight=1)

    button_Backward = Button(image_movement_canvas, text="Previous Figure", font="RobotoRoman-ExtraBold", borderwidth=0,
                           bg="#ECEFF1", command=lambda: backward())
    button_Backward.place(relwidth=0.499, relx=0, relheight=1)
    #
    button_Forward = Button(image_movement_canvas, text="Next Figure", font="RobotoRoman-ExtraBold", borderwidth=0,
                           bg="#ECEFF1", command=lambda: forward())
    button_Forward.place(relwidth=0.499, relx=0.505, relheight=1)
    button_line = Label(image_movement_canvas, width=450, bg="#000000")
    button_line.place(relwidth=0.003, relx=0.5, relheight=1)
    def forward():
        updatePlot(figure.newestFigure("Forward"))
        LogObject.button_logger.append("Forward")
        LogObject.timerButton_logger.append(LogObject.dateTime())

    def backward():
        updatePlot(figure.newestFigure("Backward"))
        LogObject.button_logger.append("Backward")
        LogObject.timerButton_logger.append(LogObject.dateTime())
    # #####################################################

    ####################    On exit #################################################################

    def on_closing():
        print('close')
        folder.RenameLogFolder()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.bind('<Return>', lambda event: _on_enter_pressed(event))
    window.resizable(True, True)
    window.mainloop()
