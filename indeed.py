from tkinter import*
import tkinter.messagebox

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal =Tk()
cal.title("Ramu Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="yellow", justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="7",command=lambda:btnClick(7),bg="light blue").grid(row=1,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="8",command=lambda:btnClick(8),bg="light blue").grid(row=1,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="9",command=lambda:btnClick(9),bg="light blue").grid(row=1,column=2)

Addition=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="+",command=lambda:btnClick("+"),bg="light blue").grid(row=1,column=3)
#---------------------------------------------------------------------

btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="4",command=lambda:btnClick(4),bg="light blue").grid(row=2,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="5",command=lambda:btnClick(5),bg="light blue").grid(row=2,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="6",command=lambda:btnClick(6),bg="light blue").grid(row=2,column=2)

Subtraction=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="-",command=lambda:btnClick("-"),bg="light blue").grid(row=2,column=3)
#---------------------------------------------------------------------

btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="1",command=lambda:btnClick(1),bg="light blue").grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="2",command=lambda:btnClick(2),bg="light blue").grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="3",command=lambda:btnClick(3),bg="light blue").grid(row=3,column=2)

Mutiply=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="*",command=lambda:btnClick("*"),bg="light blue").grid(row=3,column=3)

#------------------------------------------------------------------------------------------

btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="0",command=lambda:btnClick(0),bg="light blue").grid(row=4,column=0)

btnClear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="C",bg="light blue",command= btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="=",bg="light blue",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20,'bold'),
           text="/",command=lambda:btnClick("/"),bg="light blue").grid(row=4,column=3)
#----------------------------------------------------------------------------------------------


def iExit():
    iExit = tkinter.messagebox.askyesno("Calculator", "Confrim do you want to exit?")
    if iExit > 0:
        cal.destroy()
        return

def Standerd():
    cal.resizable(width = False, height = False)
    cal.geometry("480x568+0+0")

def Scientiffic():
    cal.resizable(width = False, height = False)
    cal.geometry("944x568+0+0")
    
    

menubar = Menu(cal)

filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standerd", command = Standerd)
filemenu.add_command(label = "Scientiffic", command = Scientiffic)
filemenu.add_separator()
filemenu.add_command(label = "Close", command = iExit)

editmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")



cal.mainloop()
