import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image


def buttonAction(n):
    print(n)

#essa classe possibilita criar botoes com altura e largura maximas
class FixedButton(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master)
        # self.rowconfigure(0, minsize=kwargs.pop('height', None))
        # self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = tk.Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

class App(tk.Tk):
    def __init__(self):
        super().__init__()
                
        #configurações da janela principal
        self.geometry("800x500")
        self.title('Urna Eletrônica')
        self.resizable(0,0)

        #define font geral do projeto 
        self.font = font.Font(size=12)

        #definindo frames
        self.pad_frame = tk.Frame(self, bg="black", width=250, height=400, pady=3, padx=1)
        self.image_frame = tk.Frame(self, bg="white", width=450, height=300, pady=3, padx=1)
        #posicionando frames
        self.pad_frame.grid(column=1, row = 0, sticky="news")
        self.image_frame.grid(column=0, row = 0, sticky="news")
        
        self.create_buttons()
        self.showImage()

    def create_buttons(self):
        
        #ao usar uma imagem 1x1 como bg, é possível definir tamanho absoluto do botão
        numericButtons = []
        self.pad_frame.grid(column=1, sticky="news")
        numericButtons.append(tk.Button(self.pad_frame, text=0, command=lambda: buttonAction(0), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=1, command=lambda: buttonAction(1), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=2, command=lambda: buttonAction(2), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=3, command=lambda: buttonAction(3), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=4, command=lambda: buttonAction(4), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=5, command=lambda: buttonAction(5), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=6, command=lambda: buttonAction(6), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=7, command=lambda: buttonAction(7), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=8, command=lambda: buttonAction(8), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=9, command=lambda: buttonAction(9), bg="black", fg="white", height=2, width=5))

        #define seu posicionamento na grade
        numericButtons[0].grid(column=3, row=3, pady=5)
        numericButtons[1].grid(column=2, row=0, pady=5, sticky="e")
        numericButtons[2].grid(column=3, row=0, pady=5)
        numericButtons[3].grid(column=4, row=0, pady=5, sticky="w")
        numericButtons[4].grid(column=2, row=1, pady=5, sticky="e")
        numericButtons[5].grid(column=3, row=1, pady=5)
        numericButtons[6].grid(column=4, row=1, pady=5, sticky="w")
        numericButtons[7].grid(column=2, row=2, pady=5, sticky="e")
        numericButtons[8].grid(column=3, row=2, pady=5)
        numericButtons[9].grid(column=4, row=2, pady=5, sticky="w")


        branco = tk.Button(self.pad_frame, text='BRANCO', bg='white', fg='black', width=8, height=1)
        corrige = tk.Button(self.pad_frame, text='CORRIGE', bg='orange', fg='black', width=8, height=1)
        confirma = tk.Button(self.pad_frame, text='CONFIRMA', bg='green', fg='black', width=8, height=2)
        branco.grid(column=2, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        corrige.grid(column=3, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        confirma.grid(column=4, row=5, sticky="news", padx=(5,5), pady=(5,5))

    def showImage(self):
        image = Image.open("resources/exemplo.jpg")
        image = image.resize((300, 300))
        tkImage = ImageTk.PhotoImage(image)
        label1 = tk.Label(self.image_frame, image=tkImage)
        label1.image = tkImage
        label1.grid(column = 0, row = 0, rowspan=6, padx=(5,5), pady=(5,5))


if __name__ == "__main__":
    app = App()
    app.mainloop()        


# canvas = tk.Canvas(root, width=300, height=600)
# canvas.grid(columnspan=3, rowspan=)