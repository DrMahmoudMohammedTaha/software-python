
# # problem - 1 - canvas
# import tkinter as tk
# parent = tk.Tk()
# canvas_width = 100
# canvas_height = 80
# w = tk.Canvas(parent, width=canvas_width,height=canvas_height)
# w.pack()
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y, fill="#476042")
# parent.mainloop()

# # problem - 2 - checkbox
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# my_boolean_var = tk.BooleanVar()
# my_checkbutton = ttk.Checkbutton( text="Check when the option True",variable=my_boolean_var)
# my_checkbutton.bind("<Button-1>", func=lambda e: print("binder worked"))
# my_checkbutton.pack()
# root.mainloop()

# # problem - 3 - listbox
# import tkinter as tk
# parent = tk.Tk()
# parent.geometry("250x200")
# label1 = tk.Label(parent,text = "A list of my students")
# listbox = tk.Listbox(parent)
# listbox.insert(1,"Ahmed")
# listbox.insert(2, "Mohammed")
# listbox.insert(3, "Hend")
# listbox.insert(4, "Hayam")
# label1.pack()
# listbox.pack()
# parent.mainloop()

# # problem - 4 - textbox
import tkinter as tk
parent = tk.Tk()
parent.geometry("400x250")
name = tk.Label(parent, text = "Name").place(x = 30, y = 50)
email = tk.Label(parent, text = "User ID").place(x = 30, y = 90)
password = tk.Label(parent, text = "Password").place(x = 30, y = 130)
sbmitbtn = tk.Button(parent, text = "Submit", activebackground = "green", activeforeground = "blue").place(x = 120, y = 170)
entry1 = tk.Entry(parent).place(x = 85, y = 50)
entry2 = tk.Entry(parent).place(x = 85, y = 90)
entry3 = tk.Entry(parent).place(x = 90, y = 130)
# show="*"
parent.mainloop()

# # problem - 5 - radiobutton
# import tkinter as tk
# parent = tk.Tk()
# parent.title("Radiobutton ")
# parent.geometry('350x200')
# radio1 = tk.Radiobutton(parent, text='First', value=1)
# radio2 = tk.Radiobutton(parent, text='Second', value=2)
# radio3 = tk.Radiobutton(parent, text='Third', value=3)
# radio1.grid(column=0, row=0)
# radio2.grid(column=1, row=0)
# radio3.grid(column=2, row=0)
# parent.mainloop()

# # tab menues
# from tkinter import *
# def donothing():
#     filewin = Toplevel(root)
#     button = Button(filewin, text="Do nothing button")
#     button.pack()
# root = Tk()
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label="New", command = donothing)
# filemenu.add_command(label = "Open", command = donothing)
# filemenu.add_command(label = "Save", command = donothing)
# filemenu.add_command(label = "Save as...", command = donothing)
# filemenu.add_command(label = "Close", command = donothing)
# filemenu.add_separator()
# filemenu.add_command(label = "Exit", command = root.quit)
# menubar.add_cascade(label = "File", menu = filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label = "Undo", command = donothing)
# editmenu.add_separator()
# editmenu.add_command(label = "Cut", command = donothing)
# editmenu.add_command(label = "Copy", command = donothing)
# editmenu.add_command(label = "Paste", command = donothing)
# editmenu.add_command(label = "Delete", command = donothing)
# editmenu.add_command(label = "Select All", command = donothing)
# menubar.add_cascade(label = "Edit", menu = editmenu)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label = "Help Index", command = donothing)
# helpmenu.add_command(label = "About...", command = donothing)
# menubar.add_cascade(label = "Help", menu = helpmenu)
# root.config(menu = menubar)
# root.mainloop()