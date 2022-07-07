import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

resources = "../resources/"

def buttonAction(n):
    print(n)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
                
        #configurações da janela principal
        self.geometry("700x400")
        self.title('Urna Eletrônica')
        self.resizable(0,0)

        #grade da janela
        self.columnconfigure(0, weight=5)
        for i in range(5):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=2)

        #fonte base do programa

        self.create_buttons()
        self.showImage()

    def create_buttons(self):
        numericButtons = []
        #define forma dos botões
        numericButtons.append(tk.Button(self, text=0, command=lambda: buttonAction(0), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=1, command=lambda: buttonAction(1), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=2, command=lambda: buttonAction(2), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=3, command=lambda: buttonAction(3), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=4, command=lambda: buttonAction(4), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=5, command=lambda: buttonAction(5), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=6, command=lambda: buttonAction(6), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=7, command=lambda: buttonAction(7), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=8, command=lambda: buttonAction(8), bg='black', fg='white'))
        numericButtons.append(tk.Button(self, text=9, command=lambda: buttonAction(9), bg='black', fg='white'))

        #define seu posicionamento na grade
        numericButtons[0].grid(column=3, row=3, sticky="news")
        numericButtons[1].grid(column=2, row=0, sticky="news")
        numericButtons[2].grid(column=3, row=0, sticky="news")
        numericButtons[3].grid(column=4, row=0, sticky="news")
        numericButtons[4].grid(column=2, row=1, sticky="news")
        numericButtons[5].grid(column=3, row=1, sticky="news")
        numericButtons[6].grid(column=4, row=1, sticky="news")
        numericButtons[7].grid(column=2, row=2, sticky="news")
        numericButtons[8].grid(column=3, row=2, sticky="news")
        numericButtons[9].grid(column=4, row=2, sticky="news")


        branco = tk.Button(self, text='BRANCO', bg='white', fg='black')
        corrige = tk.Button(self, text='CORRIGE', bg='orange', fg='black')
        confirma = tk.Button(self, text='CONFIRMA', bg='green', fg='black')
        branco.grid(column=2, row=5, sticky="news", padx=(5,5), pady=(5,5))
        corrige.grid(column=3, row=5, sticky="news", padx=(5,5), pady=(5,5))
        confirma.grid(column=4, row=5, sticky="news", padx=(5,5), pady=(5,5))

    def showImage(self):
        image = Image.open("resources/exemplo.jpg")
        image = image.resize((300, 300))
        tkImage = ImageTk.PhotoImage(image)
        label1 = tk.Label(self, image=tkImage)
        label1.image = tkImage
        label1.grid(column = 0, row=0, rowspan=6, padx=(5,5), pady=(5,5))


if __name__ == "__main__":
    app = App()
    app.mainloop()        


# canvas = tk.Canvas(root, width=300, height=600)
# canvas.grid(columnspan=3, rowspan=)