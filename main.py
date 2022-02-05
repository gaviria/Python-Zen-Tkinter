from tkinter import *

class MyApp:
  def __init__(self, root):
    root.title("My App")
    root.geometry("500x400")
    root.maxsize(1000,800)

    label = Label(root, text="Some Label Text")
    label.pack()

    label.configure(text="New Label Text",font=("Courrier",40))

    entry_text = StringVar()
    entry = Entry(root,textvariable=entry_text)
    entry.pack()

    label["textvariable"] = entry_text

root = Tk()
MyApp(root)

root.mainloop()