# importing module
import time
from tkinter import *
from tkinter.ttk import *

# importing strftime function to retrieve system.
from time import strftime
from time import *
version = "0.0.0.1.3"
# create a window
root = Tk()
root.title('Digital Clock | Developed by : Noxious')

# Size of the window by default
root.geometry('735x300+50+50')


# display time on the label
def digital_clock():
    string = strftime("%H:%M:%S")
    text.config(text=string)
    text.after(1000, digital_clock)


# Customize the label
text = Label(root, font=('times', 150, 'bold'))

digital_clock()

# center the clock
text.pack(anchor='center')

root.mainloop()
print("Clock version: " + version)
# Bug reported : The clock doesn't show the hour.
