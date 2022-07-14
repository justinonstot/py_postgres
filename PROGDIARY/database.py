
import sqlite3
connection = sqlite3.connect("PROGDIARY\data.db")

entries = [] 

def create_table():
    with connection:  # uses context manager to handle commit/rollback of the transaction.
        connection.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, content TEXT, publication_date TEXT);')

def add_entry(entry_content, entry_date):
    # query = f"INSERT INTO entries VALUES (NULL,?,?');"
    # print(query)
    with connection:
        connection.execute("INSERT INTO entries VALUES (NULL,?,?);", (entry_content, entry_date))

def get_entries():
    return entries
