from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry('400x250+440+220')
root.config(bg='misty rose')

def calc():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers!", bg='salmon', font=('Arial',16))
        return

    op=operation_var.get()

    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if num2==0:
            result_label.config(text="Can not divide by zero!", bg='salmon', font=('Arial', 16))
        else:
            result=num1/num2
    return result_label.config(text=f"Result: {result}", bg='white')
    
label1=Label(root, text="Number 1:", font='Arial', bg='white')
label1.grid(row=0, column=0, padx=10, pady=5)
entry1=Entry(root, font='Arial')
entry1.grid(row=0, column=1, padx=10,pady=5)

label2=Label(root, text="Number 2:", font='Arial', bg='white')
label2.grid(row=1, column=0, padx=10, pady=5)
entry2=Entry(root, font='Arial')
entry2.grid(row=1, column=1, padx=10, pady=5)

operation_var=StringVar()
operation_var.set("+")
label3=Label(root, text="Operation:", font='Arial', bg='white')
label3.grid(row=2, column=0, padx=10, pady=5)
operations_frame=Frame(root)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add=Radiobutton(operations_frame, text="+   ", variable=operation_var, value="+")
radio_add.config(font=15)
radio_add.pack(side=LEFT)
radio_sub=Radiobutton(operations_frame, text="-   ", variable=operation_var, value="-")
radio_sub.config(font=15)
radio_sub.pack(side=LEFT)

radio_mul=Radiobutton(operations_frame, text="*   ", variable=operation_var, value="*")
radio_mul.config(font=15)
radio_mul.pack(side=LEFT)
radio_div=Radiobutton(operations_frame, text="/   ", variable=operation_var, value="/")
radio_div.config(font=15)
radio_div.pack(side=LEFT)

submit_button=Button(root, bg='white', text="Calculate", command=calc, font='Arial')
submit_button.grid(row=3, column=0, columnspan=2, pady=8)
result_label=Label(root, text="Result: ", bg='white', font='Arial')
result_label.grid(row=4, column=0, columnspan=2, pady=5)
root.mainloop()
