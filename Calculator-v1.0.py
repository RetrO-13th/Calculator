# RetrO_13th Calculator version 1.0
# Using Tkinter GUI

from tkinter import *

expression = "" # globally declare the expression variable

def click(s_number) -> None: # Method to update expression
    global expression

    expression += str(s_number)
    equation.set(expression) # update the expression by using set method

def result() -> None:
    global expression

    try:
        result = str(eval(expression)) # eval function evaluate the expression
        equation.set(result)

        expression = "" # initialze the expression variable by empty string

    except:
        equation.set(" Error") # print error when somthing's wrong
        expression = ""

def clear() -> None: # Methode to clear the contents
    global expression

    expression = ""
    equation.set("")

def window(): # Method to display calsulator
    global equation

    window = Tk() # create a GUI window
    window.configure(background="#708d81") # set the background colour of GUI window
    window.title(" RetrO_13th Calculator") # set the title of GUI window
    window.geometry("325x480") # set the size of GUI window

    equation = StringVar() # StringVar() is the variable class

    # create the text entry box for showing the expression
    expression_window = Entry(
        window, 
        textvariable=equation,
        )

    # grid method is used for placing the widgets at respective positions in table like structure
    expression_window.grid(
        columnspan=4,
        ipadx=100,
        ipady=15
    )

    # create a Buttons and place at a particular location inside the root window .when user press the button, the command orfunction affiliated to that button is executed
    button_0 = Button(
        window,
        text=" 0 ",
        fg="white",
        bg="#001427",
        command=lambda: click(0),
        width=10,
        height=5
    )

    button_0.grid(
        row=5,
        column=0
    )

    button_1 = Button(
        window,
        text=" 1 ",
        fg="white",
        bg="#001427",
        command=lambda: click(1),
        width=10,
        height=5
    )

    button_1.grid(
        row=4,
        column=0
    )

    button_2 = Button(
        window,
        text=" 2 ",
        fg="white",
        bg="#001427",
        command=lambda: click(2),
        width=10,
        height=5
    )

    button_2.grid(
        row=4,
        column=1
    )

    button_3 = Button(
        window,
        text=" 3 ",
        fg="white",
        bg="#001427",
        command=lambda: click(3),
        width=10,
        height=5
    )

    button_3.grid(
        row=4,
        column=2
    )

    button_4 = Button(
        window,
        text=" 4 ",
        fg="white",
        bg="#001427",
        command=lambda: click(4),
        width=10,
        height=5
    )

    button_4.grid(
        row=3,
        column=0
    )

    button_5 = Button(
        window,
        text=" 5 ",
        fg="white",
        bg="#001427",
        command=lambda: click(5),
        width=10,
        height=5
    )

    button_5.grid(
        row=3,
        column=1
    )

    button_6 = Button(
        window,
        text=" 6 ",
        fg="white",
        bg="#001427",
        command=lambda: click(6),
        width=10,
        height=5
    )

    button_6.grid(
        row=3,
        column=2
    )

    button_7 = Button(
        window,
        text=" 7 ",
        fg="white",
        bg="#001427",
        command=lambda: click(7),
        width=10,
        height=5
    )

    button_7.grid(
        row=2,
        column=0
    )

    button_8 = Button(
        window,
        text=" 8 ",
        fg="white",
        bg="#001427",
        command=lambda: click(8),
        width=10,
        height=5
    )

    button_8.grid(
        row=2,
        column=1
    )

    button_9 = Button(
        window,
        text=" 9 ",
        fg="white",
        bg="#001427",
        command=lambda: click(9),
        width=10,
        height=5
    )

    button_9.grid(
        row=2,
        column=2
    )

    button_minus = Button(
        window,
        text=" - ",
        fg="white",
        bg="#001427",
        command=lambda: click(" - "),
        width=10,
        height=5
    )

    button_minus.grid(
        row=3,
        column=3
    )

    button_plus = Button(
        window,
        text=" + ",
        fg="white",
        bg="#001427",
        command=lambda: click(" + "),
        width=10,
        height=5
    )

    button_plus.grid(
        row=4,
        column=3
    )

    button_multiply = Button(
        window,
        text=" * ",
        fg="white",
        bg="#001427",
        command=lambda: click(" * "),
        width=10,
        height=5
    )

    button_multiply.grid(
        row=5,
        column=3
    )

    button_divide = Button(
        window,
        text=" / ",
        fg="white",
        bg="#001427",
        command=lambda: click(" / "),
        width=10,
        height=5
    )

    button_divide.grid(
        row=5,
        column=2
    )

    button_equal = Button(
        window,
        text=" = ",
        fg="white",
        bg="#001427",
        command=result,
        width=10,
        height=5
    )

    button_equal.grid(
        row=6,
        column=3
    )

    button_dot = Button(
        window,
        text=" . ",
        fg="white",
        bg="#001427",
        command=lambda: click("."),
        width=10,
        height=5
    )

    button_dot.grid(
        row=5,
        column=1
    )

    button_clear = Button(
        window,
        text=" CLR ",
        fg="white",
        bg="#8d0801",
        command=clear,
        width=10,
        height=5
    )

    button_clear.grid(
        row=2,
        column=3
    )

    window.mainloop() # start the GUI



if __name__ == "__main__":
    window()