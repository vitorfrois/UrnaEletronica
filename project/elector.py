
class Elector:

    def __init__(self):
        self.name = ""
        self.cpf = 0
        self.voted = False
    
    def get_name(self):
        return self.name

    def get_cpf(self):
        return self.cpf

    def add_name(self, name):
        self.name = name

    def add_cpf(self, cpf):      
        self.cpf = cpf

    def set_voted(self, bool_value):
        self.voted = bool_value

    def get_voted(self):
        return self.voted
    
