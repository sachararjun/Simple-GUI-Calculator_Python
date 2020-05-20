from tkinter import *
import math

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def btnClear():
    global operator
    operator = ""
    txt_input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    txt_input.set(sumup)
    operator = ""

def btnPM(numbers):
    global operator
    operator = math.sqrt(float(textDisplay.get()))
    txt_input.set(operator)

calc = Tk()
calc.title("Calculator")
calc.resizable(width = False, height = False)
operator = ""
txt_input = StringVar()
textDisplay = Entry(calc, font=('arial', 27, 'bold'), textvariable = txt_input, bd = 20,
                 insertwidth = 2, bg = "pale green", justify = 'right').grid(columnspan=5)

# Row 1
button7 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="7", command=lambda:btnClick(7))
button7.grid(row=1,column=0)

button8 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnClick(8))
button8.grid(row=1,column=1)

button9 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnClick(9))
button9.grid(row=1,column=2)

buttonAdd = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="+", command=lambda:btnClick("+"))
buttonAdd.grid(row=1,column=3)

buttonDot = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text=".", command=lambda:btnClick("."))
buttonDot.grid(row=1,column=4)

# R0w 2
button4 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="4", command=lambda:btnClick(4))
button4.grid(row=2,column=0)

button5 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="5", command=lambda:btnClick(5))
button5.grid(row=2,column=1)

button6 = Button(calc, padx=16,pady=16, bd=8, bg="light grey",fg="black", font=('arial', 20, 'bold'), text="6", command=lambda:btnClick(6))
button6.grid(row=2,column=2)

buttonSub = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="-", command=lambda:btnClick("-"))
buttonSub.grid(row=2,column=3)

buttonRem = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="%", command=lambda:btnClick("%"))
buttonRem.grid(row=2,column=4)

# R0w 3
button1 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="1", command=lambda:btnClick(1))
button1.grid(row=3,column=0)

button2 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="2", command=lambda:btnClick(2))
button2.grid(row=3,column=1)

button3 = Button(calc, padx=16,pady=16, bd=8, bg="light grey", fg="black", font=('arial', 20, 'bold'), text="3", command=lambda:btnClick(3))
button3.grid(row=3,column=2)

buttonMul = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="*", command=lambda:btnClick("*"))
buttonMul.grid(row=3,column=3)

buttonPow = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="^", command=lambda:btnClick("**"))
buttonPow.grid(row=3,column=4)

# R0w 4
button0 = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0))
button0.grid(row=4,column=0)

buttonClr = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="C", command=btnClear)
buttonClr.grid(row=4,column=1)

buttonEqu = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="=", command=btnEquals)
buttonEqu.grid(row=4,column=2)

buttonDiv = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="/", command=lambda:btnClick("/"))
buttonDiv.grid(row=4,column=3)

buttonPM = Button(calc, padx=16,pady=16, bd=8, bg='#A877BA', fg="black", font=('arial', 20, 'bold'), text="π", command=lambda:btnClick(math.pi))
buttonPM.grid(row=4,column=4)

calc.mainloop()
