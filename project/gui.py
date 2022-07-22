import tkinter as tk
import tkinter.font as font
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkinter import ttk
import pygame
from database import DatabaseElector, DatabaseCandidates

from candidate import *

candidates_list = []
electors_list = []
dbCandidates = DatabaseCandidates()
dbElectors = DatabaseElector()

def nada():
    pass

class UrnaFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.pad_frame = tk.Frame(self, bg="black", width=250, height=400, pady=3, padx=1)
        self.image_frame = tk.Frame(self, width=450, height=400, pady=3, padx=1)
        self.instructions_frame = tk.Frame(self, height=40)
        # posicionando frames
        self.pad_frame.grid(column=1, row = 0, sticky="news")
        self.image_frame.grid(column=0, row = 0, sticky="news")
        self.instructions_frame.grid(column=0, row=1, columnspan=2, sticky="news")
        
        self.create_buttons()
        self.create_image_frame()
        #value é uma variavel que carrega o input atual da urna
        self.value = ""
        self.votes_count = 0
        self.cargos = ("Presidente", "Governador", "Deputado Estadual", "Deputado Federal")
        self.cargos_n = (2, 2, 4, 4, -1)

    #funçao que é chamada toda vez que um botao numerico é ativado
    def button_action(self, n):
        if(len(self.value) >= self.cargos_n[self.votes_count] or self.votes_count == 4):
            return
        #atualiza o valor de value
        self.value += str(n)
        self.update_image_frame()
        print(self.value)
        #se houver um candidato com o valor atual, mostra sua foto e nome
        for candidate in candidates_list:
            if(candidate.get_number() == self.value):
                self.update_image_frame(candidate)

        if(len(self.value) == self.cargos_n[self.votes_count]):
            self.show_instructions()
        else:
            self.destroy_instructions()

    #reseta os valores 
    def corrige_button(self):
        self.value = ""
        print(self.value)
        self.update_image_frame()
        self.destroy_instructions()

    #adiciona um voto ao candidato com o número da urna
    def confirma_button(self):
        pygame.mixer.init()
        global total_votes
        if(self.cargos_n[self.votes_count] != len(self.value)):
            return
        #if(int(self.value) == 0):
            #total_votes += 1
        #print(total_votes)
        for candidate in candidates_list:
            if(candidate.get_number() == self.value):
                print("novo voto")
                candidate.add_vote()
                total_votes += 1

        self.corrige_button()
        self.votes_count += 1
        if(self.votes_count != 4):
            self.candidateCargo.set("SEU VOTO PARA: " + self.cargos[self.votes_count])

        pygame.mixer.music.load("resources/som_urna.mp3")
        pygame.mixer.music.play(loops=0)

    #voto em branco
    def branco_button(self):
        if(len(self.value) != 0 or self.votes_count >= 4):
            return
        
        if(self.cargos_n[self.votes_count] == 2):
            self.value = "00"
        else:
            self.value = "0000"
        self.show_instructions()
        self.candidateName.set("VOTO EM BRANCO")
        print("branco")

    #função que cria os botões 
    def create_buttons(self):
        numericButtons = []
        self.pad_frame.grid(column=1, sticky="news")
        numericButtons.append(tk.Button(self.pad_frame, text=0, command=lambda: self.button_action(0), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=1, command=lambda: self.button_action(1), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=2, command=lambda: self.button_action(2), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=3, command=lambda: self.button_action(3), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=4, command=lambda: self.button_action(4), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=5, command=lambda: self.button_action(5), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=6, command=lambda: self.button_action(6), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=7, command=lambda: self.button_action(7), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=8, command=lambda: self.button_action(8), bg="black", fg="white", height=2, width=5))
        numericButtons.append(tk.Button(self.pad_frame, text=9, command=lambda: self.button_action(9), bg="black", fg="white", height=2, width=5))

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
        branco = tk.Button(self.pad_frame, text='BRANCO', bg='white', fg='black', width=8, height=1, command=self.branco_button)
        corrige = tk.Button(self.pad_frame, text='CORRIGE', bg='orange', fg='black', width=8, height=1, command=self.corrige_button)
        confirma = tk.Button(self.pad_frame, text='CONFIRMA', bg='green', fg='black', width=8, height=2, command=self.confirma_button)
        branco.grid(column=2, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        corrige.grid(column=3, row=5, sticky="sew", padx=(5,5), pady=(5,5))
        confirma.grid(column=4, row=5, sticky="news", padx=(5,5), pady=(5,5))

    #mostra as instruções de voto na tela
    def show_instructions(self):
        self.text1 = tk.Label(self.instructions_frame, text="CONFIRMA para CONFIRMAR este voto")
        self.text1.grid(column=0, row=0, sticky="w", padx=(5,5))
        self.text2 = tk.Label(self.instructions_frame, text="CORRIGE para REINICIAR este voto")
        self.text2.grid(column=0, row=1, sticky="w", padx=(5,5))

    #apaga as instruções de voto na tela    
    def destroy_instructions(self):
        try:
            self.text1.destroy()
            self.text2.destroy()
        except:
            print("Instruções ainda não foram criadas.")

    #cria o frame da imagem, que vai mostrar a imagem do candidato, seu nome e partido
    def create_image_frame(self):
        self.candidateName = tk.StringVar(self.image_frame)
        self.candidateimage_path = tk.StringVar(self.image_frame, "resources/pixel.png")
        self.candidateParty = tk.StringVar(self.image_frame, "")
        self.candidateNumber = tk.StringVar(self.image_frame, "")
        self.candidatePartyName = tk.StringVar(self.image_frame, "")
        self.candidateCargo = tk.StringVar(self.image_frame, "")
        image = Image.open(self.candidateimage_path.get())
        image = image.resize((150, 150))
        tkImage = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.image_frame, image=tkImage)
        imageLabel.image = tkImage
        imageLabel.grid(column = 0, row = 0, rowspan=6, padx=(5,5), pady=(5,5))
        info1Label = tk.Label(self.image_frame, textvariable=self.candidateCargo)
        info1Label.grid(column=0, row=6, sticky="w", padx=(5,5))
        candidateNameLabel = tk.Label(self.image_frame, textvariable=self.candidateName)
        candidateNameLabel.grid(column=0, row=7, sticky="w", padx=(5,5))
        candidateNumberLabel = tk.Label(self.image_frame, textvariable=self.candidateNumber)
        candidateNumberLabel.grid(column=0, row=8, sticky="w", padx=(5,5))
        candidatePartyName = tk.Label(self.image_frame, textvariable=self.candidatePartyName)
        candidatePartyName.grid(column=0, row=9, sticky="w", padx=(5,5))
        self.candidateCargo.set("SEU VOTO PARA: Presidente")
        self.candidateName.set("Nome: ")
        self.candidateNumber.set("Número: ")
        self.candidateimage_path.set("resources/pixel.png")
        self.candidatePartyName.set("Número: ")

    #atualiza o frame da imagem
    def update_image_frame(self, candidate:Candidate()=None):
        if(candidate != None and len(self.value) == self.cargos_n[self.votes_count]):
            self.candidateName.set("Nome: " + candidate.get_name())
            self.candidateNumber.set("Número: " + candidate.get_number())
            self.candidateimage_path.set(candidate.get_image())
            self.candidatePartyName.set("Partido: " + candidate.get_party())
        else:
            if(self.cargos_n[self.votes_count] == len(self.value)):
                self.candidateNumber.set("Nome:" + self.value)
                self.candidateName.set("NÚMERO ERRADO")
                self.candidatePartyName.set("VOTO NULO")
            else:
                self.candidateName.set("Nome: ")
                self.candidateNumber.set("Número: " + self.value)
                self.candidateimage_path.set("resources/pixel.png")
                self.candidatePartyName.set("Número: ") #tinha uma virgula aqui

        self.candidateParty.set(self.value)
        image = Image.open(self.candidateimage_path.get())
        image = image.resize((150, 150))
        tkImage = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self.image_frame, image=tkImage)
        imageLabel.image = tkImage
        imageLabel.grid(column = 0, row = 0, rowspan=6, padx=(5,5), pady=(5,5))
        
    def newEleitor(self):
        self.eleitor_frame = tk.Frame(self, pady=3, padx=1)
        name = tk.Label(self, text="Nome: ")
        

class DBInsertFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(column=0, row=0, sticky="news")
        self.create_db_frame()

    #função para selecionar o arquivo de imagem
    def select_file(self):
        filetypes = (
            ('Arquivos de imagem', '*.jpg'),
            ('All files', '*.*')
        )

        self.image_path = fd.askopenfilename(
            title='Escolha uma imagem: ',
            initialdir='~',
            filetypes=filetypes
        )
        print(self.image_path)

    #apaga os campos
    def clear_entry(self):
        self.name_field.delete(0, 'end')
        self.party_field.delete(0, 'end')
        self.num_field.delete(0, 'end')
        self.cargo_field.set("")
        self.image_path = ""
        self.submit_text.set("Inserir")

    #tenta inserir o candidato com os dados detalhados na lista
    def submit_candidate(self):
        num = self.num_field.get()

        for candidate in candidates_list:
            if(candidate.get_number() == num):
                self.db_info_label.set("Já existe um candidato com o número inserido.")
                return
                
        if (self.name_field.get() == "" or
            self.party_field.get() == "" or
            self.num_field.get() == "" or
            self.cargo_field.get() == "" or
            self.image_path == ""):
            self.db_info_label.set("Preencha todos os campos.")
            print("empty input")
            return

        if(not num.isnumeric()):
            self.db_info_label.set("O campo de número deve conter números.")
            return

        if(self.cargo_field.get() == 'Presidente' or self.cargo_field.get() == 'Governador'):
            if(len(num) != 2):
                self.db_info_label.set("O número do partido deve conter 2 algarismos.")
                return

        if(self.cargo_field.get() == 'Deputado Federal' or self.cargo_field.get() == 'Deputado Estadual'):
            if(len(num) != 4):
                self.db_info_label.set("O número do partido deve conter 4 algarismos.")
                return
        

        new_candidate = Candidate()
        new_candidate.add_image(self.image_path)
        new_candidate.add_name(self.name_field.get())
        new_candidate.add_number(self.num_field.get())
        new_candidate.add_party(self.party_field.get()) #adicionando o partido
        new_candidate.add_cargo(self.cargo_field.get()) #add cargo
        candidates_list.append(new_candidate)
        self.db_info_label.set("Candidato Inserido com Sucesso!")
        self.clear_entry()            

    #cria o frame da database
    def create_db_frame(self):
        #label para mostrar informações
        heading = tk.Label(self, text="Inserção de candidatos")
        name = tk.Label(self, text="Nome: ")
        party = tk.Label(self, text="Partido: ")
        num = tk.Label(self, text="Número: ")
        cargo = tk.Label(self, text="Cargo: ")

        #o botão para escolher a imagem do candidato
        browse_button = tk.Button(self, text="Escolher Imagem", command=self.select_file)
    
        #entry é utilizada para ler informações
        self.name_field = tk.Entry(self)
        self.party_field = tk.Entry(self)
        self.num_field = tk.Entry(self)
        self.cargo_field = tk.StringVar()
        self.cargo_cb = ttk.Combobox(self, textvariable=self.cargo_field) #add cargo
        self.cargo_cb['values'] = ('Presidente', 'Governador', 'Deputado Federal', 'Deputado Estadual')
        self.cargo_cb['state'] = 'readonly'
    
        self.submit_text = tk.StringVar(self, "Inserir")
        submit = tk.Button(self, textvariable=self.submit_text, command=self.submit_candidate)

        self.db_info_label = tk.StringVar(self, "")
        db_info_label = tk.Label(self, textvariable=self.db_info_label)

        #posiciona os objetos na grade        
        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        party.grid(row=2, column=0)
        num.grid(row=3, column=0)
        cargo.grid(row=4, column = 0) #grid cargo
        self.name_field.grid(row=1, column=1, ipadx="100")
        self.party_field.grid(row=2, column=1, ipadx="100")
        self.num_field.grid(row=3, column=1, ipadx="100")
        self.cargo_cb.grid(row=4, column=1, sticky="w") #add cargo field
        browse_button.grid(row=5, column=1, sticky="w")
        submit.grid(row=6, column=1)
        db_info_label.grid(column=1, row=7, padx=(5,5))

class DBRemoveFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(column=0, row=0, sticky="news")
        self.create_db_frame()

    #apaga os campos
    def clear_entry(self):
        self.name_field.set("")

    #tenta inserir o candidato com os dados detalhados na lista
    def submit_candidate(self):
        for candidate in candidates_list:
            print(candidate.get_name() + self.name_field.get())
            if candidate.get_name() == self.name_field.get():
                candidates_list.remove(candidate)
                print(candidates_list)
                self.db_info_label.set("Candidato Removido com Sucesso!")
        self.clear_entry()            

    #cria o frame da database
    def create_db_frame(self):
        #label para mostrar informações
        heading = tk.Label(self, text="Remoção de Candidatos")
        name = tk.Label(self, text="Nome: ")

        #entry é utilizada para ler informações
        self.name_field = tk.StringVar()
        self.cargo_cb = ttk.Combobox(self, textvariable=self.name_field) #add cargo
        candidates_name_list = []
        for candidate in candidates_list:
            candidates_name_list.append(candidate.get_name())
        self.cargo_cb['values'] = tuple(candidates_name_list)
        self.cargo_cb['state'] = 'readonly'
    
        self.submit_text = tk.StringVar(self, "Remover")
        submit = tk.Button(self, textvariable=self.submit_text, command=self.submit_candidate)

        self.db_info_label = tk.StringVar(self, "")
        db_info_label = tk.Label(self, textvariable=self.db_info_label)

        #posiciona os objetos na grade        
        heading.grid(row=0, column=1)
        name.grid(row=1, column=0)
        self.cargo_cb.grid(row=1, column=1, ipadx="100")
        submit.grid(row=6, column=1)
        db_info_label.grid(column=1, row=7, padx=(5,5))

class VotesFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(column=0, row=0, sticky="news")
        self.table = ttk.Treeview(self)
        self.table.grid()
        self.table['columns'] = ('Candidato', 'Votos')
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("Candidato")
        self.table.column("Votos")
        self.table.heading("Candidato", text="Candidato")
        self.table.heading("Votos", text="Votos")
        global total_votes
        total_votes = 0
    
    def create_vote_frame(self):
        self.table.delete(*self.table.get_children())
        for candidate in candidates_list:
            candidate_votes = candidate.get_votes()
            print(candidate_votes)
            if(total_votes != 0):
                votes = str(candidate_votes) + " (" + str((candidate_votes/total_votes)*100) + "%)"
            else:
                votes = total_votes
            self.table.insert(parent='', index='end', text='', values=(candidate.get_name() + ' (' + candidate.get_cargo() + ')', votes))        



class WelcomeFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid(column=0, row=0, sticky="news")
        self.create_welcome_frame()
    
    def create_welcome_frame(self):
        image = Image.open("resources/urna.jpg")
        image = image.resize((400, 250))
        tkImage = ImageTk.PhotoImage(image)
        imageLabel = tk.Label(self, image=tkImage)
        imageLabel.image = tkImage
        imageLabel.grid(column = 0, row = 0, padx=(5,5), pady=(5,5), sticky="news")
        heading = tk.Label(self, text="SIMULADOR DE URNA ELETRÔNICA")
        heading.grid(row=1, column=0, sticky="news")

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
                
        #configurações da janela principal
        # self.geometry("600x400")
        self.title('Urna Eletrônica')
        self.resizable(0,0)
        #adiciona candidatos para teste
        self.add_test_candidates()
        #inicializa os frames
        self.urna_frame = UrnaFrame(self)
        self.urna_frame.grid(column=0, row=0)
        self.db_frame = DBInsertFrame(self)
        self.db_frame.grid(column=0, row=0, sticky="news")
        self.db_remove_frame = DBRemoveFrame(self)
        self.db_remove_frame.grid(column=0, row=0, sticky="news")
        self.votes_frame = VotesFrame(self)
        self.votes_frame.grid(column=0, row=0, sticky="news")
        self.welcome_frame = WelcomeFrame(self)
        self.welcome_frame.grid(column=0, row=0, sticky="news")

        #adiciona o menu na janela principal 
        self.add_menu()


    def show_votes(self):
        self.votes_frame.create_vote_frame()
        self.votes_frame.lift()

    #sistema de menu
    def add_menu(self):
        menubar = tk.Menu(self)
        
        #menu de gerenciamento de arquivos
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Novo", command=newElection)
        menu_file.add_command(label="Abrir", command=openElection)
        menu_file.add_command(label="Salvar", command=saveElection)     

        #menu de opções
        menu_options = tk.Menu(menubar, tearoff=0)
        menu_options.add_command(label="Iniciar Votação", command=self.urna_frame.lift) 
        menu_options.add_command(label="Inserir Candidato", command=self.db_frame.lift)  
        menu_options.add_command(label="Remover Candidato", command=self.db_remove_frame.lift)        
        menu_options.add_command(label="Mostrar Votos", command=self.show_votes)        
        
        
        #adiciona todos menus ao menu principal
        menubar.add_cascade(label="Arquivo", menu=menu_file)
        menubar.add_cascade(label="Opções", menu=menu_options)
        menubar.add_command(label="Sair", command=self.destroy)

        self.config(menu=menubar)

    def add_test_candidates(self):
        #adiciona alguns candidatos a lista para teste
        #lula
        lula = Candidate()
        lula.add_image("resources/lula.jpg")
        lula.add_name("Lula")
        lula.add_number("13")
        lula.add_cargo("Presidente")
        candidates_list.append(lula)
        #bolsonaro
        bolsonaro = Candidate()
        bolsonaro.add_image("resources/bolsonaro.jpg")
        bolsonaro.add_name("Bolsonaro")
        bolsonaro.add_number("22")
        candidates_list.append(bolsonaro)

def newElection():
    dbCandidates.remove_all_candidates()
    dbElectors.remove_all_electors()
    global candidates_list
    candidates_list = []
    global electors_list
    electors_list = []

def openElection():
    newElection()

    global candidates_list
    global electors_list

    candidates_list = dbCandidates.candidates()
    electors_list =  dbElectors.electors()

def saveElection():
    for candidate in candidates_list:
        dbCandidates.insert_candidate(candidate)
    print(dbCandidates.candidates())
    for elector in electors_list:
        dbElectors.insert_elector(elector)
    print(dbElectors.electors())


if __name__ == "__main__":
    app = GUI()
    app.mainloop()        


# canvas = tk.Canvas(root, width=300, height=600)
# canvas.grid(columnspan=3, rowspan=)