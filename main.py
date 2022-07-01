# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

from tkinter import *

# Setting Up The Window
window = Tk()
window.title("Miles To KM Calculator")
window.minsize(width = 210, height = 100)
window.config(padx = 20, pady = 20)

# Function to Convert Miles to KM
def convert():
    miles_num = float(miles_dist.get())
    km_dist.config(text = f"{round(miles_num * 1.609, 4)}")

# Ask for distance in Miles
miles_dist = Entry(window, width = 10)
miles_dist.grid(row = 0, column = 1)

miles_text = Label(text = "Miles")
miles_text.grid(row = 0, column = 2)

# Display the distance in KM
result_text = Label(text = "Is Equal To")
result_text.grid(row = 1, column = 0)

km_dist = Label(text = "0")
km_dist.grid(row = 1, column = 1)

km_text = Label(text = "KM")
km_text.grid(row = 1, column = 2)

# Convert Button
convert_btn = Button(text = "Convert", command = convert)
convert_btn.grid(row = 2, column = 1)

window.mainloop()