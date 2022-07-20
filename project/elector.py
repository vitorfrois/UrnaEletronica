from msilib.schema import Class
import string


class elector:

    def __init__(self):
        self.name = ""
        self.code = ""
    
    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def add_name(self, name):
        if name.isalpha():
            self.name = name
        else:
            # erro

    def add_code(self, code):      
        if code.isdigit():
            self.code = code
        else:
            # erro
            