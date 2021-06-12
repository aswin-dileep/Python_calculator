from tkinter import *

expression = ""


window = Tk()
window.configure(background="black")

window.title("calculator")

window.geometry("250x250")

screen = StringVar()

in_screen = Entry(window, textvariable=screen)

in_screen.grid(padx=5, pady=15, ipadx=55, ipady=10)
screen.set('enter')

def press(num):
    global expression

    expression = expression + str(num)

    screen.set(expression)

def equal():

    try:
        global expression

        total = str(eval(expression))

        screen.set(total)

        expression = ""

    except:

        screen.set("error")

        expression = ""

def clear():

    global expression

    screen.set("")

    expression = ""


btn1 = Button(text="1", width = "5", height= "2", command=lambda: press(1))
btn2 = Button(text="2", width = "5", height= "2",command=lambda: press(2))
btn3 = Button(text="3", width = "5", height= "2",command=lambda: press(3))
btnp = Button(text="+", width = "5", height= "2",command=lambda: press("+"))
btn4 = Button(text="4", width = "5", height= "2",command=lambda: press(4))
btn5 = Button(text="5", width = "5", height= "2",command=lambda: press(5))
btn6 = Button(text="6", width = "5", height= "2",command=lambda: press(6))
btns = Button(text="-", width = "5", height= "2",command=lambda: press("-"))
btn7 = Button(text="7", width = "5", height= "2",command=lambda: press(7))
btn8 = Button(text="8", width = "5", height= "2",command=lambda: press(8))
btn9 = Button(text="9", width = "5", height= "2",command=lambda: press(9))
btnd = Button(text="/", width = "5", height= "2",command=lambda: press("/"))
btn0 = Button(text="0", width = "5", height= "2",command=lambda: press(0))
btnm = Button(text="*", width = "5", height= "2",command=lambda: press("X"))
btne = Button(text="=", width = "5", height= "2",command=equal)
btnc = Button(text="C", width = "5", height= "2",command=clear)


btn1.place(x=10,y=60)
btn2.place(x=60,y=60)
btn3.place(x=110,y=60)
btnp.place(x=160,y=60)
btn4.place(x=10,y=110)
btn5.place(x=60,y=110)
btn6.place(x=110,y=110)
btns.place(x=160,y=110)
btn7.place(x=10,y=160)
btn8.place(x=60,y=160)
btn9.place(x=110,y=160)
btne.place(x=160,y=160)
btn0.place(x=10,y=210)
btnc.place(x=60,y=210)


window.mainloop()