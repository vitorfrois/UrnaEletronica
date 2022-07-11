from candidate import Candidates

class Urna:
    
    def __init__(self, electionName) -> None:
        self.electionName = electionName # nome da eleição (ideia é o programa armazenar dados de eleições diferentes)
        self.number = "" # self.number é uma variavel que carrega o input atual da urna
        self.candidates = [] #lista de candidados

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def remove_candidate(self, candidate):
        if candidate in self.candidates:
            self.candidates.remove(candidate)
        else: raise Exception;

    def get_candidates(self):
        return self.candidates

    def add_number(self): #chama botoes da gui, n sei como faz
        pass

    def get_number(self): 
        return self.number