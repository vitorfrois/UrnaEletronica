import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image

from candidate import *

def nada():
    pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
                
        #configurações da janela principal
        # self.geometry("600x400")
        self.title('Urna Eletrônica')
        self.resizable(0,0)

        #define font geral do projeto 
        self.font = font.Font(size=12)
        #definindo frames
        self.urna = tk.Frame(self, bg="white")
        self.db_frame = tk.Frame(self)
        self.db_frame.grid(column=0, row=0)
        pages = {"db": self.db_frame, "urna": self.urna}
        self.urna.grid()

        # self.databaseFrame()
        # self.db_frame.tkraise()

        self.pad_frame = tk.Frame(self.urna, bg="black", width=250, height=400, pady=3, padx=1)
        self.image_frame = tk.Frame(self.urna, width=450, height=400, pady=3, padx=1)
        self.instructions_frame = tk.Frame(self.urna, height=40)
        # posicionando frames
        self.pad_frame.grid(column=1, row = 0, sticky="news")
        self.image_frame.grid(column=0, row = 0, sticky="news")
        self.instructions_frame.grid(column=0, row=1, columnspan=2, sticky="news")
        
        #adiciona alguns candidatos a lista para teste
        self.candidatesList = []
        #lula
        lula = Candidate()
        lula.add_image("resources/lula.jpg")
        lula.add_name("Lula")
        lula.add_number("13")
        self.candidatesList.append(lula)
        #bolsonaro
        bolsonaro = Candidate()
        bolsonaro.add_image("resources/bolsonaro.jpg")
        bolsonaro.add_name("Bolsonaro")
        bolsonaro.add_number("22")
        self.candidatesList.append(bolsonaro)

        #value é uma variavel que carrega o input atual da urna
        self.value = ""

        #adiciona os componentes no frame principal
        self.addMenu()
        self.create_buttons()
        self.createImageFrame()
        self.db_frame.tkraise()

    #funçao que é chamada toda vez que um botao numerico é ativado
    def buttonAction(self, n):
        if(len(self.value) >= 2):
            return
        #atualiza o valor de value
        self.value += str(n)
        self.updateImageFrame()
        print(self.value)
        #se houver um candidato com o valor atual, mostra sua foto e nome
        for candidate in self.candidatesList:
            if(candidate.get_number() == self.value):
                self.updateImageFrame(candidate)

        if(len(self.value) == 2):
            self.showInstructions()
        else:
            self.destroyInstructions()


    #reseta value
    def corrigeButton(self):
        self.value = ""
        print(self.value)
        self.updateImageFrame()
        self.destroyInstructions()


    #por enquanto não faz nada
    def confirmaButton(self):
        for candidate in self.candidatesList:
            if(candidate.get_number() == self.value):
                candidate.add_vote()
        self.corrigeButton()

    def brancoButton(self):
        if(len(self.value) >= 2):
            return
        self.value = ""
        self.showInstructions()
        self.candidateName.set("VOTO EM BRANCO")
        print("branco")

    #função que cria os botões 
    #pensando em como modularizar essa parte
    def create_buttons(self):
        numericButtons = []
        self.pad_frame.grid(column=1, sticky="news")
        numericButtons.append(tk.Button(self.pad_frame, text=0, command=lambda: self.buttonAction(0), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=1, command=lambda: self.buttonAction(1), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=2, command=lambda: self.buttonAction(2), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=3, command=lambda: self.buttonAction(3), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=4, command=lambda: self.buttonAction(4), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=5, command=lambda: self.buttonAction(5), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=6, command=lambda: self.buttonAction(6), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=7, command=lambda: self.buttonAction(7), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=8, command=lambda: self.buttonAction(8), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=9, command=lambda: self.buttonAction(9), bg="black", fg="white", height=2, width=5))

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

        #os botoes secundarios
        branco = tk.Button(self.pad_frame, text='BRANCO', bg='white', fg='black', width=8, height=1, command=self.brancoButton)
        corrige = tk.Button(self.pad_frame, text='CORRIGE', bg='orange', fg='black', width=8, height=1, command=self.corrigeButton)
        confirma = tk.Button(self.pad_frame, text='CONFIRMA', bg='green', fg='black', width=8, height=2, command=self.confirmaButton)
        branco.grid(column=2, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        corrige.grid(column=3, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        confirma.grid(column=4, row=5, sticky="news", padx=(5,5), pady=(5,5))

    def showInstructions(self):
        self.text1 = tk.Label(self.instructions_frame, text="CONFIRMA para CONFIRMAR este voto")
        self.text1.grid(column=0, row=0, sticky="w", padx=(5,5))
        self.text2 = tk.Label(self.instructions_frame, text="CORRIGE para REINICIAR este voto")
        self.text2.grid(column=0, row=1, sticky="w", padx=(5,5))
    
    def destroyInstructions(self):
        try:
            self.text1.destroy()
            self.text2.destroy()
        except:
            print("Instruções ainda não foram criadas.")

    #cria o frame da imagem, que vai mostrar a imagem do candidato, seu nome e partido
    def createImageFrame(self):
        self.candidateName = tk.StringVar(self.image_frame)
        self.candidateImagePath = tk.StringVar(self.image_frame, "resources/pixel.png")
        self.candidateParty = tk.StringVar(self.image_frame, "")
        self.candidatePartyName = tk.StringVar(self.image_frame, "")
        image = Image.open(self.candidateImagePath.get())
        image = image.resize((150, 150))
        tkImage = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.image_frame, image=tkImage)
        imageLabel.image = tkImage
        imageLabel.grid(column = 0, row = 0, rowspan=6, padx=(5,5), pady=(5,5))
        info1Label = tk.Label(self.image_frame, text="SEU VOTO PARA: ")
        info1Label.grid(column=0, row=6, sticky="w", padx=(5,5))
        candidatePartyLabel = tk.Label(self.image_frame, textvariable=self.candidateParty)
        candidatePartyLabel.grid(column=0, row=7, padx=(5,5))
        candidateNameLabel = tk.Label(self.image_frame, textvariable=self.candidateName)
        candidateNameLabel.grid(column=0, row=8, sticky="w", padx=(5,5))
        candidatePartyName = tk.Label(self.image_frame, textvariable=self.candidatePartyName)
        candidatePartyName.grid(column=0, row=9, sticky="w", padx=(5,5))

    #atualiza o frame do candidato
    def updateImageFrame(self, candidate:Candidate()=None):
        if(candidate != None):
            self.candidateName.set("Nome: " + candidate.get_name())
            self.candidateImagePath.set(candidate.get_image())
            self.candidatePartyName.set("Partido: " + candidate.get_name())
        else:
            self.candidateImagePath.set("resources/pixel.png")
            if(len(self.value) == 2):
                self.candidateName.set("NÚMERO ERRADO")
                self.candidatePartyName.set("VOTO NULO")
            else:
                self.candidateName.set("")
                self.candidatePartyName.set("");

        self.candidateParty.set(self.value)
        image = Image.open(self.candidateImagePath.get())
        image = image.resize((150, 150))
        tkImage = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.image_frame, image=tkImage)
        imageLabel.image = tkImage
        imageLabel.grid(column = 0, row = 0, rowspan=6, padx=(5,5), pady=(5,5))

        

    #sistema de menu, mas por enquanto não há nada significativo
    def addMenu(self):
        menubar = tk.Menu(self)
        
        #menu de gerenciamento de arquivos
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Novo", command=nada)
        menu_file.add_command(label="Abrir", command=nada)
        menu_file.add_command(label="Salvar", command=nada)    

        #menu de opções
        menu_options = tk.Menu(menubar, tearoff=0)
        menu_options.add_command(label="Iniciar Votação", command=self.urna.tkraise) 
        menu_options.add_command(label="Inserir Candidato", command=self.db_frame.lift)        

        
        #adiciona todos menus ao menu principal
        menubar.add_cascade(label="Arquivo", menu=menu_file)
        menubar.add_cascade(label="Opções", menu=menu_options)
        menubar.add_command(label="Sair", command=self.db_frame.lift)

        self.config(menu=menubar)

    def select_file():
        filetypes = (
            ('Image Files', '*.jpg'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Escolha a imagem do candidato',
            initialdir='.',
            filetypes=filetypes)

    # def switchFrames(self, name):
    #     page = pages[name]


    def databaseFrame(self):
        heading = tk.Label(self.db_frame, text="Inserção de candidatos", bg="light green")

        # create a Name tk.label
        name = tk.Label(self.db_frame, text="Nome: ", bg="light green")
    
        # create a Course tk.label
        party = tk.Label(self.db_frame, text="Partido: ", bg="light green")
    
        # create a Semester tk.label
        num = tk.Label(self.db_frame, text="Número: ", bg="light green")


        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        party.grid(row=2, column=0)
        num.grid(row=3, column=0)
    
        # create a text entry box
        # for typing the information
        name_field = tk.Entry(self.db_frame)
        party_field = tk.Entry(self.db_frame)
        num_field = tk.Entry(self.db_frame)
    
        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        name_field.grid(row=1, column=1, ipadx="100")
        party_field.grid(row=2, column=1, ipadx="100")
        num_field.grid(row=3, column=1, ipadx="100")
    
        # create a Submit Button and place into the root window
        submit = tk.Button(self.db_frame, text="Submit", fg="Black", bg="Red")
        submit.grid(row=8, column=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()        


# canvas = tk.Canvas(root, width=300, height=600)
# canvas.grid(columnspan=3, rowspan=)