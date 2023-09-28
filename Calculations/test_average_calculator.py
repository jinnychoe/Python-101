# Test Average Calculator GUI

# This program creates a graphical user interface (GUI) to input five test scores,
# calculate their average and sum total, and display the results.

import tkinter

class TestAVG:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Test Score Average Calculator")

        # Create and pack the frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.sum_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.avg_frame.pack()
        self.sum_frame.pack()
        self.button_frame.pack()

        # Create and pack the widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame, text="Enter the score for test 1: ")
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for test 2
        self.test2_label = tkinter.Label(self.test2_frame, text="Enter the score for test 2: ")
        self.test2_entry = tkinter.Entry(self.test2_frame, width=10)
        self.test2_label.pack(side="left")
        self.test2_entry.pack(side="left")

        # Create and pack the widgets for test 3
        self.test3_label = tkinter.Label(self.test3_frame, text="Enter the score for test 3: ")
        self.test3_entry = tkinter.Entry(self.test3_frame, width=10)
        self.test3_label.pack(side="left")
        self.test3_entry.pack(side="left")

        # Create and pack the widgets for test 4
        self.test4_label = tkinter.Label(self.test4_frame, text="Enter the score for test 4: ")
        self.test4_entry = tkinter.Entry(self.test4_frame, width=10)
        self.test4_label.pack(side="left")
        self.test4_entry.pack(side="left")

        # Create and pack the widgets for test 5
        self.test5_label = tkinter.Label(self.test5_frame, text="Enter the score for test 5: ")
        self.test5_entry = tkinter.Entry(self.test5_frame, width=10)
        self.test5_label.pack(side="left")
        self.test5_entry.pack(side="left")

        # Create and pack the widgets for the average
        self.result_label = tkinter.Label(self.avg_frame, text="Average: ")
        self.avg = tkinter.StringVar()  # to update avg_label
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)

        self.result_label.pack(side="left")
        self.avg_label.pack(side="left")

        # Create and pack the widgets for the sum total
        self.result_label2 = tkinter.Label(self.sum_frame, text="Total: ")
        self.sum = tkinter.StringVar()  # to update sumtot_label
        self.sumtot_label = tkinter.Label(self.sum_frame, textvariable=self.sum)

        self.result_label2.pack(side="left")
        self.sumtot_label.pack(side="left")

        # Create and pack the button widgets
        self.calc_button = tkinter.Button(self.button_frame, text="Calculate", command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Start the main loop
        tkinter.mainloop()

    # Calculate method is a callback function for calc_button widget
    def calc_avg(self):
        # Get 5 test scores and store them in variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())
        self.test5 = float(self.test5_entry.get())

        # Calculate average
        self.average = (self.test1 + self.test2 + self.test3 + self.test4 + self.test5) / 5.0

        # Calculate sum total
        self.sumtot = self.test1 + self.test2 + self.test3 + self.test4 + self.test5

        # Update avg_label and sumtot_label widgets
        self.avg.set(self.average)
        self.sum.set(self.sumtot)

# Create an instance of TestAVG class
if __name__ == "__main__":
    test_avg = TestAVG()

