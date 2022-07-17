class Candidate:

    def __init__(self) -> None:
        self.name = ""
        self.number = -1
        self.image = ""
        self.votes = 0

    def add_name(self, name) -> None:
        self.name = name

    def add_number(self, number) -> None:
        self.number = number

    def add_image(self, image) -> None:
        self.image = image

    def add_vote(self) -> None:
        self.votes += 1

    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number

    def get_image(self):
        return self.image

    def get_votes(self):
        return self.votes
    
