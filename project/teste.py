import tkinter as tk
import tkinter.font as tkFont

def bigger():
    size = font.cget("size")
    font.configure(size=size+2)

def smaller():
    size = font.cget("size")
    size = max(2, size-2)
    font.configure(size=size)

root = tk.Tk()
font = tkFont.Font(family="Helvetica", size=12)

toolbar = tk.Frame(root)
container = tk.Frame(root)

toolbar.pack(side="top", fill="x")
container.pack(side="top", fill="both", expand=True)

bigger = tk.Button(toolbar, text="Bigger", command=bigger)
smaller = tk.Button(toolbar, text="Smaller", command=smaller)

bigger.pack(side="left")
smaller.pack(side="left")

pixel = tk.PhotoImage(width=1, height=1)
for row in range(3):
    container.grid_rowconfigure(row, weight=1)
    for column in range(3):
        container.grid_columnconfigure(column, weight=1)
        button = tk.Button(container, font=font, text="x",
            image=pixel, compound="center", width=20, height=20)
        button.grid(row=row, column=column)

root.mainloop()