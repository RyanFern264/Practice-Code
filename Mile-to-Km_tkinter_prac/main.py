import tkinter
from tkinter import *

def button_clicked():
    miles = int(input.get())
    km = miles * 1.6
    km = str(km)
    km_num_label.config(text=km)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=100, height=100)
#increase padding around each element
window.config(padx=20, pady=20)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

km_num_label = Label(text="0")
km_num_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

#Buttons
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


#Entry
input = Entry(width=10)
input.grid(column=2, row=1)


window.mainloop()