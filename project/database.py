import sqlite3
from candidate import Candidate
from elector import Elector

class DatabaseCandidates:

    def __init__(self, databaseName="db/candidates.db") -> None:
        self.conn = sqlite3.connect(databaseName)
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS candidates (name text, number integer, image text, votes integer) ")

    def insert_candidate(self, candidate):
        with self.conn:
            if not self.search_candidate(candidate):
                self.c.execute("INSERT INTO candidates VALUES (:name, :number, :image, :votes)",
                    {'name': candidate.name,
                    'number': candidate.number,
                    'image': candidate.image,
                    'votes': candidate.votes})

    def open_database(self, databaseName):
        self.conn.close()
        self.conn = sqlite3.connect(databaseName)
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS candidates (name text, number integer, image text, votes integer) ")

    def search_candidate(self, candidate):
        self.c.execute("SELECT rowid FROM candidates WHERE name = :name AND number = :number", {'name': candidate.name, 'number': candidate.number})
        data = self.c.fetchone()
        if data is None:
            return False
        else:
            return True

    def candidates(self):
        self.c.execute("SELECT * FROM candidates")
        return self.c.fetchall()
            
    def update_votes(self, candidate):
        with self.conn:
            self.c.execute("UPDATE candidates SET votes = :votes WHERE name = :name AND number = :number", 
                {'name': candidate.name,
                'number': candidate.number,
                'votes': candidate.votes})

    def remove_candidate(self, candidate):
        with self.conn:
            if self.search_candidate(candidate):
                self.c.execute("DELETE FROM candidates WHERE name = :name AND number = :number", 
                    {'name': candidate.name,
                    'number': candidate.number})

    def remove_all_candidates(self):
        with self.conn:
            self.c.execute("DELETE FROM candidates")

    def close(self):
        self.conn.close()
        
class DatabaseElector:

    def __init__(self, databaseName="electors") -> None:
        self.conn = sqlite3.connect('db/' + databaseName + '.db')
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS electors (name text, code integer) ")

    def insert_elector(self, elector):
        with self.conn:
            if not self.search_elector(elector):
                self.c.execute("INSERT INTO electors VALUES (:name, :code)",
                    {'name': elector.name,
                    'code': elector.cpf})
    
    def electors(self):
        self.c.execute("SELECT * FROM electors")
        return self.c.fetchall()

    def search_elector(self, elector):
        self.c.execute("SELECT rowid FROM electors WHERE name = :name AND code = :code", {'name': elector.name, 'code': elector.cpf})
        data = self.c.fetchone()
        if data is None:
            return False
        else:
            return True

    def remove_all_electors(self):
        with self.conn:
            self.c.execute("DELETE FROM electors")

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = DatabaseElector()
    admin = Elector()
    admin.add_cpf(1)
    admin.add_name("admin")
    db.insert_elector(admin)
    vitor = Elector()
    vitor.add_cpf(12797125622)
    vitor.add_name("Vítor Amorim Fróis")
    db.insert_elector(vitor)


