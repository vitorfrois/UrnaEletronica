from shutil import ExecError


class Candidate:

    def __init__(self) -> None:
        self.name = ""
        self.number = -1
        self.image = ""
        self.votes = 0
        self.party = ""

    def add_name(self, name) -> None:
        if name.isalpha():
            self.name = name
        else:
            raise Exception

    def add_number(self, number) -> None:
        if number.isdigit():
            self.number = number
        else:
            raise Exception

    def add_image(self, image) -> None:
        self.image = image

    def add_vote(self) -> None:
        self.votes += 1
        
    def add_party(self, party) -> None:
        if party.isalpha():
            self.party = party
        else:
            raise Exception

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
    
