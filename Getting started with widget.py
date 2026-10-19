from tkinter import *

root = Tk()

root.title("Getting Started with Widgets")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="white")

l1 = Label(root, text="WELCOME TO THINTER", fg="Navy blue", bg="white", font=("times new roman", 23, "bold"))
l1.place(x=0, y=10)