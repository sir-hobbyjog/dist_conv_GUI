from tkinter import *

TITLE = "Mile to KM Converter"
INPUT = "Miles"
OUTPUT = "KM"

window = Tk()
window.title(TITLE)
window.minsize(width=300, height=180)

result = 0

input_label = Label(text=INPUT, font=("Arial", 12, "bold"))
input_label.grid(row = 0, column=2)

output_label = Label(text=OUTPUT, font=("Arial", 12, "bold"))
output_label.grid(row = 1, column=2)

result_label = Label(text=result, font=("Arial", 12, "bold"))
result_label.grid(row = 1, column=1)

is_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_label.grid(row = 1, column=0)

def button_clicked():
    if input_label["text"] == "Miles":
        n1 = float(input.get())
        result_label.config(text=(round((n1*1.60934),2)))
    elif input_label["text"] == "KM":
        n1 = float(input.get())
        result_label.config(text=(round((n1/1.60934),2)))


def switch_button_clicked():
    if input_label["text"] == "Miles":
        input_label.config(text="KM")
        output_label.config(text="Miles")
    elif input_label["text"] == "KM":
        input_label.config(text="Miles")
        output_label.config(text="KM")

calculate_button = Button(text = "Calculate", command=button_clicked)
calculate_button.grid(row = 2, column = 1)

switch_button = Button(text = "Switch", command=switch_button_clicked)
switch_button.grid(row = 3, column = 1)

input = Entry(width = 10)
input.grid(row = 0, column=1)









window.mainloop()