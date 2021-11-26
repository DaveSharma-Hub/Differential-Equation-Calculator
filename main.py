# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import ttk

from Tools.scripts.serve import app


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import math
import matplotlib.pyplot as plt
from tkinter import *

# later use ADT arraylist to have any y^(n)
y1 = 0;  # for y'
y2 = 0;  # for y''
x1 = 0;  # for RHS


def findValue(val):
    return (x1 / y1) * val


def eulerMethod(val,iter,x0,y0):
    storage = [0] * iter
    values = [0] * iter
    h = (val-y0)/iter
    tmp = 1.0
    storage = [(y0 + (k* h)) for k in range(0, len(storage))]
    values = [y0 for k in range(0, len(values))]
    print(h)
    for x in range(0,len(storage)):
        if x>0:
            values[x] = values[x-1]+(h*findValue(storage[x-1]))
    return values

def setDE(a, b, c):
    global y1, y2, x1
    y1 = a
    y2 = b
    x1 = c


setDE(1, 0, 2)


import tkinter
answer_entry=0
answer_entry1=0
answer_entry2=0
answer_entry3=0
answer_entry4=0
answer_entry5=0
i=0
# Create the default window
root = tkinter.Tk()
root.title("Welcome to Differential Equation Calculator")
root.geometry('700x700')
value_inside=0

# Create the list of options
def mainPage():
    for widget in root.winfo_children():
        widget.destroy()

    options_list = ["Euler Method", "Option 2", "Option 3", "Option 4"]
    global value_inside
# Variable to keep track of the option
# selected in OptionMenu
    value_inside = tkinter.StringVar(root)
# Set the default value of the variable
    value_inside.set("Select an Option")
# Create the optionmenu widget and passing
# the options_list and value_inside to it.
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    submit_button = tkinter.Button(root, text='Try', command=print_answers)
    submit_button.pack()
    root.mainloop()

def eurlerSetup():
    for widget in root.winfo_children():
        widget.destroy()

    global answer_entry,answer_entry1,answer_entry2,answer_entry3,answer_entry4,answer_entry5,i
    labelEqun = StringVar()
    labelEqun.set("Equation Form: __y'=__x'")
    labelEqun = Label(root, textvariable=labelEqun, height=4)
    labelEqun.place(x=150, y=40)
    labelEqun.pack()
    directory = StringVar(None)

    labelText = StringVar()
    labelText.set("y' numerical coefficient")
    labelDir = Label(root, textvariable=labelText, height=4)
    labelDir.place(x=150, y=50)
    labelDir.pack()
    directory = StringVar(None)

    answer_entry = Entry(root, textvariable=directory, width=4)
    answer_entry.place(x=300, y=50)
    answer_entry.pack()

    labelText1 = StringVar()
    labelText1.set("x' numerical coefficient")
    labelDir1 = Label(root, textvariable=labelText1, height=4)
    labelDir1.place(x=150, rely=60)
    labelDir1.pack()
    directory1 = StringVar(None)

    answer_entry1 = Entry(root, textvariable=directory1, width=4)
    answer_entry1.place(x=300, y=60)
    answer_entry1.pack()

    labelText2 = StringVar()
    labelText2.set("x point")
    labelDir2 = Label(root, textvariable=labelText2, height=4)
    labelDir2.place(x=150, rely=70)
    labelDir2.pack()
    directory2 = StringVar(None)
    answer_entry2 = Entry(root, textvariable=directory2, width=4)
    answer_entry2.place(x=300, y=70)
    answer_entry2.pack()

    labelText3 = StringVar()
    labelText3.set("y point")
    labelDir3 = Label(root, textvariable=labelText3, height=4)
    labelDir3.place(x=150, rely=80)
    labelDir3.pack()
    directory3 = StringVar(None)
    answer_entry3 = Entry(root, textvariable=directory3, width=4)
    answer_entry3.place(x=300, y=80)
    answer_entry3.pack()

    labelText4 = StringVar()
    labelText4.set("Iterations")
    labelDir4 = Label(root, textvariable=labelText4, height=4)
    labelDir4.place(x=150, rely=90)
    labelDir4.pack()
    directory4 = StringVar(None)
    answer_entry4 = Entry(root, textvariable=directory4, width=4)
    answer_entry4.place(x=300, y=90)
    answer_entry4.pack()

    labelText5 = StringVar()
    labelText5.set("X desired value: ")
    labelDir5 = Label(root, textvariable=labelText5, height=4)
    labelDir5.place(x=150, rely=100)
    labelDir5.pack()
    directory5 = StringVar(None)
    answer_entry5 = Entry(root, textvariable=directory5, width=4)
    answer_entry5.place(x=300, y=100)
    answer_entry5.pack()

    i = IntVar(0)
    c = Checkbutton(root, text="Show Graph", variable=i)
    c.pack()
    submit_buttonInside = Button(root, text="Submit",command=setOnEurler)

    submit_buttonInside.place(x=500, y=50)
    submit_buttonInside.pack()


def setOnEurler():
    setDE(float(answer_entry.get()), 0, float(answer_entry1.get()))
    holdArray = eulerMethod(float(answer_entry5.get()), int(answer_entry4.get()),float(answer_entry2.get()), float(answer_entry3.get()))
    print(holdArray)
    print("Selected Option: {}".format(holdArray[int(answer_entry4.get())-1]))
    labelText6 = StringVar()
    labelText6.set("Desired X value is: {}".format(holdArray[int(answer_entry4.get())-1]))
    labelDir6 = Label(root, textvariable=labelText6, height=4)
    labelDir6.place(x=150, rely=100)
    labelDir6.pack()
    print(i)

    if i.get()==1:
        plt.plot(holdArray)
        plt.ylabel('Graph')
        plt.show()


    submit_buttonReturn= Button(root, text="Go Back",command=mainPage)
    submit_buttonReturn.place(x=600, y=50)
    submit_buttonReturn.pack()


def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    if value_inside.get()=='Euler Method':
        eurlerSetup()

mainPage()

# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
