
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "Clear":
        scvalue.set("")
        screen.update()

    elif text == "x":
        if scvalue.get() == "":
            pass
        else:
            scvalue.set(scvalue.get()[:-1])
            screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("900x750")
root.title("My_Calculator")
root.wm_iconbitmap("cal.ico")

# add buttons using frame

f = Frame(root,bg="gray")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar= scvalue, font= "lucida 30 bold",relief=SUNKEN)
screen.pack(fill=X, pady=10, padx=30, ipady=30)

button1 = Button(f, text= "Clear", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "x", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "%", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "/", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="gray")

button1 = Button(f, text= "7", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "8", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "9", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "*", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="gray")

button1 = Button(f, text= "4", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "5", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "6", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "-", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="gray")

button1 = Button(f, text= "1", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "2", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "3", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "+", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="gray")

button1 = Button(f, text= "00", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "0", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= ".", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

button1 = Button(f, text= "=", fg='black', bg='red', height=4, width=10)
button1.pack(side=LEFT)
button1.bind("<Button-1>", click)

f.pack()

f = Frame(root,bg="gray")

button1 = Button(f, text= "Double click for exit", fg='black', bg='red', height=4, width=33)
button1.pack()
button1.bind("<Double-1>", quit)

f.pack()
root.mainloop()