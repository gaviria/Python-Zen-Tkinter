from tkinter import *

class MyApp:
  def __init__(self, root):
    root.title("My App")
    root.geometry("500x400")
    root.maxsize(1000,800)

    label = Label(root, text="Some Label Text")
    label.pack()

root = Tk()
MyApp(root)

root.mainloop()