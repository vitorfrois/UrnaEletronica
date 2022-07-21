class Elector:

    def __init__(self):
        self.name = ""
        self.code = 0
    
    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def add_name(self, name):
        if name.isalpha():
            self.name = name
        else:
            return False

    def add_code(self, code):      
        self.code = code
    
    def __str__(self) -> str:
        string = "Eleitor {}, cpf {}".format(self.name, self.code)
        return string