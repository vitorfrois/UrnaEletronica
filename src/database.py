import sqlite3
from candidate import Candidate

conn = sqlite3.connect('../db/candidates.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS candidates (name text, number integer, image text, votes integer) """)

def insert_candidate(candidate):
    with conn:
        c.execute("INSERT INTO candidates VALUES (:name, :number, :image, :votes)",
                {'name': candidate.name,
                 'number': candidate.number,
                 'image': candidate.image,
                 'votes': candidate.votes})
            
def update_votes(candidate):
    with conn:
        c.execute("""UPDATE candidates SET votes = :votes WHERE name = :name AND number = :number""", 
                {'name': candidate.name,
                 'number': candidate.number,
                 'votes': candidate.votes})

def remove_candidate(candidate):
    with conn:
        c.execute("DELETE from candidate WHERE name = :name AND number = :number", 
                {'name': candidate.name,
                 'number': candidate.number})

conn.close()

