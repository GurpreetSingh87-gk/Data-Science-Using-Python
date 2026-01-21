# GUI - Tkinter:-

# Tkinter:- The Standard inbuilt GUI library of Python. It is used to create desktop-based
# --------  applications. Tkinter is based on the Tk GUI Toolkit.


# Basic Program to Create GUI:-
# --------------------------

# --- GUI ---

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")
root.mainloop()

print(root)
'''

# =================================================================================================

# Tkinter Widgets:- Widgets are GUI components used to built interface.
# ---------------


# 1. Label Widget:- It is used to display 'Text or Images'.
#    ------------

# Syntax:-
# -------

# tk.Label(parent, text="Message")

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Label Widget ---

lbl = tk.Label(root, text="Welcome To Tkinter")
lbl.pack()

root.mainloop()
print(root)
'''

# 2. Button Widget:- It used to create 'Action on Click'.
#    -------------

# Syntax:-
# ------

# Button(parent, text="Click", command=function)

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Button Widget ---

def show():
    print("Button Clicked")

btn = tk.Button(root, text="Click", command=show)
btn.pack()

root.mainloop()
print(root)
'''

# 3. Entry Widget:- It used to take 'Single-line user input'.
#    ------------

# Syntax:-
# ------

# tk.Entry(parent).pack()

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Entry Widget ---

entry = tk.Entry(root)
entry.pack()

root.mainloop()
print(root)
'''

# 4. Frame Widget:- It used to 'Group Related Widgets'.
#    ------------

# Syntax:-
# ------

# tk.Label(frame, text="Inside Frame").pack()

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Frame Widget ---

frame = tk.Frame()
frame.pack()

tk.Label(frame, text="Inside Frame").pack()

root.mainloop()
print(root)
'''

# 5. Checkbutton Widget:- It is used for 'Multiple Selection(True/False)'.
#    ------------------

# Syntax:-
# ------

# tk.Checkbutton(root, text="Accept Terms", variable=var).pack()

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Check Button ---

var = tk.IntVar()

chkbtn = tk.Checkbutton(root, text="Accept Terms", variable=var)
chkbtn.pack()

root.mainloop()
print(root)
'''

# 6. Canvas Widget:- It is used for 'Drawing Shapes and Graphics'.
#    -------------

# Syntax:-
# ------

# tk.Canvas(root, width=200, height=200).pack()

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

# --- Canvas Widget ---

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

canvas.create_rectangle(50, 50, 150, 150)
canvas.create_oval(60, 60, 140, 140)

root.mainloop()
print(root)
'''

# =================================================================================================

# Geometry Management: It is used for controls widget placement.
# -------------------

# 1. pack():- It arranges widgets veritcally or horizontally.
#    ------

# Options:- side(top,right,left,bottom), fill, expand.

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

label = tk.Label(root, text="Welcome To Tkinter")
'''
# A. Side:- top, left, right, bottom.
#    ----
'''
label.pack(side="top")
label.pack(side="left")
label.pack(side="right")
label.pack(side="bottom")
'''

# B. Fill:- fill accepts only tk.X or tk.Y or tk.BOTH
#    ----   Y:- works Vertical lines go up and down (y-axis)
#           X:- works Horizontal lines go left to right (x-axis) 

'''
label.pack(fill=tk.X, padx=200, pady=100)
'''

# C. Expand:- It will palce widget at center.
#    ------
'''
label.pack(expand=True)
'''

# 2. grid():- It uses row and column.
#    -----

'''
tk.Label(root, text="Name", padx=10, pady=10).grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
'''

# 3. place():- It uses absolute positioning.
#    ------

'''
label.place(x=50, y=100)

root.mainloop()
print(root)
'''

# =================================================================================================

# Binding Functions (Event Handling):- Tkinter is Event-Driven method.
# ----------------------------------

# Bind() Method:-

# Syntax:-
# ------

# widget.bind(event, user define function_name)

'''
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x400")

label = tk.Label(root, text="Welcome To Tkinter").pack()
'''

# Common Mouse Events:-
# -------------------

# 1. <Button-1> :- It will work at Left Click on Mouse.
#    ----------

'''
def mouse_click(event):
    print("Mouse Clicked at", event.x, event.y)

root.bind("<Button-1>", mouse_click)
'''

# 2. <Button-2> :- It will work at Middle Click on Mouse.
#    ---------

'''
def mouse_click(event):
    print("Mouse Clicked at", event.x, event.y)

root.bind("<Button-2>", mouse_click)
'''

# 3. <Button-3> :- It will work at Third Click on Mouse.
#    ---------

'''
def mouse_click(event):
    print("Mouse Clicked at", event.x, event.y)

root.bind("<Button-3>", mouse_click)
'''

# 4. <Double-1> :- It will work at Double Click on Mouse.
#    ---------

'''
def mouse_click(event):
    print("Mouse Clicked at", event.x, event.y)

root.bind("<Double-1>", mouse_click)

root.mainloop()
print(root)
'''

# =================================================================================================

# Building a Complete GUI Interface(Mini Project):-
# -----------------------------------------------

'''
import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Email Id").grid(row=1, column=0, padx=10, pady=10)

Username = tk.Entry(root)
Password = tk.Entry(root)
Email = tk.Entry(root, show="*")

Username.grid(row=0, column=1)
Password.grid(row=1, column=1)
Email.grid(row=2, column=1)

def login():
    print("Username:",Username.get())
    print("Password:",Password.get())
    print("Email Id:",Email.get())
    
tk.Button(root, text="Login", command=login).grid(row=3, column=1, pady=10)

root.mainloop()
print(root)
'''



