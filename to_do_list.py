import tkinter as tk
from tkinter import messagebox

def add_task():
    tesk = entry.get()
    if tesk:
        listbox.insert(tk.END,tesk)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","please enter a tesk")
    
def delete_task():
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)
    except:
        messagebox.showwarning("warning","please select a tesk to delete")

#create a window
win = tk.Tk()
win.geometry("800x600")
win.title("to do list")

#create and add widget

entry = tk.Entry(win, width=30)
entry.pack()

add_button = tk.Button(win, text="add tesk",command=add_task)
add_button.pack()

delete_button = tk.Button(win, text="delete task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(win, selectmode=tk.SINGLE, width=40,height=10)
listbox.pack()

win.mainloop()