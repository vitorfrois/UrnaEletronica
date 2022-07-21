import sqlite3
from candidate import Candidate
from elector import Elector

class DatabaseCandidates:

    def __init__(self, databaseName="candidates") -> None:
        self.conn = sqlite3.connect('../db/' + databaseName + '.db')
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS candidates (name text, number integer, image text, votes integer) ")

    def insert_candidate(self, candidate):
        with self.conn:
            self.c.execute("INSERT INTO candidates VALUES (:name, :number, :image, :votes)",
                {'name': candidate.name,
                'number': candidate.number,
                'image': candidate.image,
                'votes': candidate.votes})

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
        self.conn = sqlite3.connect('../db/' + databaseName + '.db')
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS electors (name text, code integer) ")

    def insert_elector(self, elector):
        with self.conn:
            self.c.execute("INSERT INTO electors VALUES (:name, :code)",
                {'name': elector.name,
                'code': elector.code})
    
    def electors(self):
        self.c.execute("SELECT * FROM electors")
        return self.c.fetchall()

    def search_elector(self, elector):
        self.c.execute("SELECT rowid FROM electors WHERE name = ? AND code = ?", (elector.name, elector.code))
        data = self.c.fetchone()
        if data is None:
            print("num achei não uai")
            return False
        else:
            print("achei")
            return True

    def remove_all_electors(self):
        with self.conn:
            self.c.execute("DELETE FROM electors")

    def close(self):
        self.conn.close()

# db = DatabaseCandidates()
# cand1 = Candidate("Théozin", 9, "AAA")
# cand2 = Candidate("Maju", 16, "BBB")
# cand3 = Candidate("Vergaças", 3, "CCC")

# db.remove_all_candidates()
# db.insert_candidate(cand1)
# db.insert_candidate(cand2)
# db.insert_candidate(cand3)

# print(db.candidates())

# db.remove_candidate(cand1)

# print(db.candidates())

# cand2.add_vote()

# db.update_votes(cand2)

# print(db.candidates())

# db.close()

db2 = DatabaseElector()

elec1 = Elector()
elec1.add_name = "Théozin"
elec1.add_code = 1234

db2.remove_all_electors()
db2.insert_elector(elec1)
print(db2.electors())

db2.search_elector(elec1)

db2.close()







