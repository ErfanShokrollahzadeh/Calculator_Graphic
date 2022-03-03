from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(width=False,height=False)

operator = ""
text_input = StringVar()

#===============================================================================================================
text_display = Entry(root,textvariable=text_input,bd=30,insertwidth=4,bg='powder blue',justify=RIGHT,font=('arial',20,'bold'))
text_display.grid(columnspan=4)

#==========================================FUNCSIONS==========================================
def btn_Click(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def btn_clear():
    global operator
    operator = ""
    text_input.set("")

def btn_equal():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""
#==========================================BUTTONS============================================
btn7 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='7',command=lambda:btn_Click(7))
btn7.grid(row=1,column=0)

btn8 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='8',command=lambda:btn_Click(8))
btn8.grid(row=1,column=1)

btn9 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='9',command=lambda:btn_Click(9))
btn9.grid(row=1,column=2)

btn4 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='4',command=lambda:btn_Click(4))
btn4.grid(row=2,column=0)

btn5 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='5',command=lambda:btn_Click(5))
btn5.grid(row=2,column=1)

btn6 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='6',command=lambda:btn_Click(6))
btn6.grid(row=2,column=2)

btn1 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='1',command=lambda:btn_Click(1))
btn1.grid(row=3,column=0)

btn2 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='2',command=lambda:btn_Click(2))
btn2.grid(row=3,column=1)

btn3 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='3',command=lambda:btn_Click(3))
btn3.grid(row=3,column=2)

btn0 = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='0',command=lambda:btn_Click(0))
btn0.grid(row=4,column=0)

addition = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='+',command=lambda:btn_Click('+'))
addition.grid(row=1,column=3)

minuse = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='-',command=lambda:btn_Click('-'))
minuse.grid(row=2,column=3)

multy = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='*',command=lambda:btn_Click('*'))
multy.grid(row=3,column=3)

devision = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='/',command=lambda:btn_Click('/'))
devision.grid(row=4,column=3)

btnC = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='C',command=lambda:btn_clear())
btnC.grid(row=4,column=1)

equal = Button(root,padx=16,pady=16,bd=8,foreground='black',font=('arial',20,'bold'),text='=',command=lambda:btn_equal())
equal.grid(row=4,column=2)

root.mainloop()