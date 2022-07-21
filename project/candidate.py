
class Candidate:

    def __init__(self) -> None:
        self.name = ""
        self.number = -1
        self.image = ""
        self.votes = 0
        self.party = ""
        self.cargo = ""

    def add_name(self, name) -> None:
        if name.isalpha():
            self.name = name
        else:
            raise Exception

    def add_number(self, number) -> None:
        self.number = number
    
    #adicionar cargo ao politico
    def add_cargo(self, cargo) -> None:
        self.cargo = cargo #tirei o exception pq tava dando erro

    def add_image(self, image) -> None:
        self.image = image

    def add_vote(self) -> None:
        self.votes += 1
        
    def add_party(self, party) -> None:
        self.party = party

    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number

    def get_image(self):
        return self.image

    def get_votes(self):
        return self.votes
        
    def get_party(self):
        return self.party

    def get_cargo(self):
        return self.cargo
        
    def __str__(self) -> str:
        string = "Candidato à {}: {}, partido: {}, número: {}".format(self.cargo, self.name, self.party, self.number)
        return string


