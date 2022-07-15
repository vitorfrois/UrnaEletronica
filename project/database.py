from locale import DAY_2
import sqlite3
from candidate import Candidate

class Database:

    def __init__(self, databaseName="election") -> None:
        self.conn = sqlite3.connect('db/' + databaseName + '.db')
        self.c = self.conn.cursor()
        self.c.execute(" CREATE TABLE IF NOT EXISTS candidates (name text, number integer, image text, votes integer) ")
        self.numDatabase = 1

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

db = Database()
cand1 = Candidate("Théozin", 9, "AAA")
cand2 = Candidate("Maju", 16, "BBB")
cand3 = Candidate("Vergaças", 3, "CCC")

db.remove_all_candidates()
db.insert_candidate(cand1)
db.insert_candidate(cand2)
db.insert_candidate(cand3)

print(db.candidates())

db.remove_candidate(cand1)

print(db.candidates())

cand2.add_vote()

db.update_votes(cand2)

print(db.candidates())

db.close()

db2 = Database()
db2.close()







