from tkinter import *

root=Tk()
root.title("TO DO LIST")
root.geometry("450x330+440+220")
root.config(bg='misty rose')

head=Label(root, text="TO DO LIST 🪶", font=('Times New Roman', 16, 'bold'), bg='white')
head.grid(row=0, column=0, columnspan=2, pady=10)

label1=Label(root, text="Enter Task:", font=('Arial', 12), bg='white')
label1.grid(row=1, column=0, padx=10, pady=5, sticky=W)

task_entry=Entry(root, font=('Arial', 12), width=30)
task_entry.grid(row=1, column=1, padx=10, pady=5)

fram= Frame(root)
fram.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

task_listbox=Listbox(
    fram,
    height=8,
    width=45,
    font=('Arial', 12),
    selectbackground='#3B3B3B',
    activestyle='none'
)
task_listbox.pack()

def add_task():
    task=task_entry.get()
    if task!="":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected= task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])

btn1=Button(root, text="Add Task", command=add_task, bg='white', width=12)
btn1.grid(row=3, column=0, pady=10)
btn2=Button(root, text="Delete Task", command=delete_task, bg='white', width=12)
btn2.grid(row=3, column=1, pady=10)

root.mainloop()