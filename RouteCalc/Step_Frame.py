from Tkinter import *
import tkFont


# This file includes a class for stepFrame. It is used to display frame
# information from within the Window
class stepFrame(Frame):
    # Initialize the stepframe
    def __init__(self):
        Frame.__init__(self, width=520, highlightbackground="grey",
                       highlightcolor="grey", highlightthickness=2)

        # step values
        self.distance = DoubleVar()
        self.interval = DoubleVar()
        self.feature = StringVar()
        self.action = StringVar()
        self.note = StringVar()

        # string for printing
        self.str_klm = " Km"

        # Frame for step text
        text_frame = Frame(self, relief=FLAT, borderwidth=2, width=400,
                           height=70)
        text_frame.grid_propagate(0)
        text_frame.grid(column=1, row=0)

        # Frame for distance and interval information
        dist_frame = Frame(self, relief=GROOVE, borderwidth=1)
        dist_frame.grid(column=2, row=0, pady=0)

        # font values
        Helvetica10 = tkFont.Font(family='Times New Roman', size=10,
                                  weight='bold')
        Helvetica7 = tkFont.Font(family='Times New Roman', size=7,
                                 weight='bold')

        # Create checkbutton
        self.check = Checkbutton(self, relief=GROOVE, bd=1, justify=CENTER,
                                 state=DISABLED)
        self.check.grid(column=0, row=0, padx=10, pady=10)

        # Fill distance frame
        Label(dist_frame, textvariable=self.distance, font=Helvetica10).grid(
            column=1, row=0, padx=1, pady=5)
        Label(dist_frame, textvariable=self.interval, font=Helvetica10).grid(
            column=1, row=1, padx=1, pady=5)
        Label(dist_frame, text="dist: ", font=Helvetica7).grid(
            column=0, row=0, padx=3, pady=5)
        Label(dist_frame, text="int: ", font=Helvetica7).grid(
            column=0, row=1, padx=3, pady=5)
        Label(dist_frame, text=self.str_klm, font=Helvetica7).grid(
            column=2, row=0, padx=5, pady=10)
        Label(dist_frame, text=self.str_klm, font=Helvetica7).grid(
            column=2, row=1, padx=5, pady=10)

        # Fill text frame
        Label(text_frame, textvariable=self.feature, font=Helvetica10).grid(
            column=0, row=0, padx=2, pady=2)
        Label(text_frame, textvariable=self.action, font=Helvetica10).grid(
            column=0, row=1, padx=2, pady=2)
        Label(text_frame, textvariable=self.note, font=Helvetica10).grid(
            column=0, row=2, padx=2, pady=2)


# Main used for testing of this file
if __name__ == '__main__':
    root = Tk()
    root.title("Route Calculator")
    root.geometry("600x400")

    fr_cur_step = stepFrame()
    fr_cur_step.distance.set(32)
    fr_cur_step.interval.set(.8)
    fr_cur_step.feature.set("Feature")
    fr_cur_step.action.set("Action")
    fr_cur_step.note.set("Note")
    # second_fr = speedFrame()
    # second_fr.speed.set(60)
    fr_cur_step.grid(column=0, row=0)
    # second_fr.grid(column = 4, row = 4)
    root.mainloop()
