from Tkinter import *
import tkFileDialog
import tkMessageBox
from datetime import datetime, timedelta
from Source import Route, CSVReader, Step_Frame, Speed_Frame


# Class which represents the main frame within the tkInter window, and holds all
# other sub frames and widgets
class GUI(Frame):
    # Initialize the GUI
    def __init__(self):
        Frame.__init__(self)

        # Create step frames for the current step and the next two steps
        self.fr_cur_step = Step_Frame.stepFrame()
        self.fr_next_step_one = Step_Frame.stepFrame()
        self.fr_next_step_two = Step_Frame.stepFrame()

        # Arrange the step frames in the GUI
        self.fr_cur_step.grid(column=0, columnspan=10, rowspan=4)
        self.fr_next_step_one.grid(column=0, columnspan=10, rowspan=4)
        self.fr_next_step_two.grid(column=0, columnspan=10, rowspan=4)

        # Add a button to call the distance prediction and arrange it in the GUI
        self.btn_predict = Button(text="Predict Distance", fg="blue",
                                  command=self.predict_step, state=DISABLED)
        self.btn_predict.grid(column=11, row=0, padx=15)

        # Add the label for the predicted distance
        self.predicted_step = StringVar()
        Label(textvariable=self.predicted_step).grid(column=11, row=1)

        # Add a frame for the current speed and arrange it in the GUI
        self.fr_speed = Speed_Frame.speedFrame()
        self.fr_speed.grid(column=11, row=12)

        # Add three entry fields for speed, time, and distance
        Label(text="Enter speed, e.g. 50").grid(column=0, row=12)
        self.input_speed = Entry()
        self.input_speed.grid(column=0, row=13)

        Label(text="Enter time, e.g. 1:32:00").grid(column=1, row=12)
        self.input_time = Entry()
        self.input_time.grid(column=1, row=13)

        Label(text="Enter distance, e.g. 1680").grid(column=2, row=12)
        self.input_dist = Entry()
        self.input_dist.grid(column=2, row=13)

        # Add button to calculate given two of three inputs
        Button(text="Calculate", command=self.calculate).grid(column=1, row=14)

    # Advance the step in the route and refresh the step frames
    def check_off_step(self):
        Route.advance_step()
        self.refresh_steps()

    # Get the current steps and assign them to the appropriate step frames
    def refresh_steps(self):
        cur_step_obj = Route.get_cur_step()
        step_one_obj, step_two_obj = Route.get_next_two()
        self.assign_step(self.fr_cur_step, cur_step_obj)
        self.assign_step(self.fr_next_step_one, step_one_obj)
        self.assign_step(self.fr_next_step_two, step_two_obj)
        self.fr_cur_step.check.deselect()
        self.fr_speed.speed_set(cur_step_obj.speed)

    # Fill in the attributes of the step object in the provided step frame
    def assign_step(self, step_frame, step_obj):
        step_frame.distance.set(step_obj.distance)
        step_frame.interval.set(step_obj.interval)
        step_frame.feature.set(step_obj.feature)
        step_frame.action.set(step_obj.action)
        step_frame.note.set(step_obj.note)

    # Call the function to predict the step the car will be at
    def predict_step(self, end_time=None):
        self.predicted_step.set(
            str(Route.get_predicted_step(end_time=end_time).distance if end_time
                else Route.get_predicted_step().distance))

    # Call the function that assigns the start of day step number
    def start_day(self):
        Route.set_day_start()

    # Prompt for the file to import, read the CSV, and load the steps
    def on_import(self):
        file_name = file_picker()
        if file_name:
            CSVReader.import_CSV(file_name)
            self.refresh_steps()
            self.activate_buttons()

    # Prompt for the file to read, read the CSV, and load the steps
    def on_read(self):
        file_name = file_picker()
        if file_name:
            CSVReader.read_CSV(file_name)
            self.refresh_steps()
            self.activate_buttons()

    # Activate the buttons that are grayed out
    def activate_buttons(self):
        self.fr_cur_step.check.config(state=NORMAL, command=self.check_off_step)
        self.btn_predict.config(state=NORMAL)

    # Based on which text entries are filled in, call the appropriate function
    def calculate(self):
        if not self.input_speed.get() and self.input_dist.get() \
                and self.input_time.get():
            time = datetime.strptime(self.input_time.get(), "%H:%M:%S").time()
            t_delta = timedelta(hours=time.hour, minutes=time.minute,
                                seconds=time.second)
            # Insert the result of the speed function into the speed field
            self.input_speed.insert(0, self.get_speed(
                float(self.input_dist.get()), t_delta))

        elif not self.input_dist.get() and self.input_time.get() \
                and self.input_speed.get():
            time = datetime.strptime(self.input_time.get(), "%H:%M:%S").time()
            t_delta = timedelta(hours=time.hour, minutes=time.minute,
                                seconds=time.second)
            # Insert the result of the distance function into the distance field
            self.input_dist.insert(0, self.get_distance(
                float(self.input_speed.get()), t_delta))

        elif not self.input_time.get() and self.input_speed.get() \
                and self.input_dist.get():
            # Insert the result of the time function into the time field
            self.input_time.insert(0, self.get_time(
                float(self.input_speed.get()), float(self.input_dist.get())))

    # Returns speed needed to go the provided distance in the provided time
    def get_speed(self, distance, time):
        return distance / (time.total_seconds() / 3600)

    # Returns distance gone given the provided speed for the provided time
    def get_distance(self, speed, time):
        return speed * time.total_seconds() / 3600

    # Returns time required to go the provided distance at the provided speed
    def get_time(self, speed, distance):
        if not speed == 0:
            return timedelta(hours=distance / speed)
        else:
            return "Undefined"


# Returns a file name chosen by the nice file picker dialog box
def file_picker():
    file_types = [('CSV', '*.csv'), ('All files', '*')]
    return tkFileDialog.askopenfilename(initialdir="../", title="Select File",
                                        filetypes=file_types)


# Creates menu bar, and the File drop down sub menu
# root is a reference to the Tk object
def set_up_menu(root, gui):
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    file_menu = Menu(menu_bar, tearoff=0)
    settings_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Read", command=gui.on_read)
    file_menu.add_command(label="Start Day", command=gui.start_day)
    file_menu.add_command(label="Export", command=CSVReader.export_CSV)
    file_menu.add_command(label="Import", command=gui.on_import)
    file_menu.add_command(label="Exit", command=onExit)

    settings_menu.add_command(label="mph <-> km/h",
                              command=gui.fr_speed.switch_units)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)


# on program close. if None, then cancel action. if True, save CSV then close
# program. If false, just close program
def onExit():
    res = tkMessageBox.askyesnocancel("Quit", "Do you want to save?")
    if res is None:
        return
    elif res:
        CSVReader.export_CSV()
    root.destroy()


# Entry point of the Route Calculator program
if __name__ == '__main__':
    root = Tk()
    root.title("RouteCalculator")
    root.resizable(width=False, height=False)
    root.geometry("775x375")
    root.protocol('WM_DELETE_WINDOW', onExit)
    gui = GUI()
    set_up_menu(root, gui)
    root.mainloop()
