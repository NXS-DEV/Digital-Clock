# importing module
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
version = "0.0.0.1.5"
# create a window
root = Tk()
root.title('Digital Clock | Developed by : Noxious')
# Size of the window by default
root.geometry('645x245+50+50')

# Create a label to display the time
time_label = Label(root, font=('Technology', 150, 'bold'), background="white", foreground="#00FFFF")
time_label.pack(fill=tk.BOTH, expand=True, anchor='center')
def digital_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    root.after(1000, digital_clock)


#update the time every second
digital_clock()

# Main loop of the program
root.mainloop()

