
import sqlite3
connection = sqlite3.connect("./data.db")

# entries = [] 

def create_table():
    with connection:  # uses context manager to handle commit/rollback of the transaction.
        connection.execute('CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);')

def add_entry(entry_content, entry_date):
    # query = f"INSERT INTO entries VALUES (NULL,?,?');"
    # print(query)
    with connection:
        connection.execute("INSERT INTO entries VALUES (?,?);", (entry_content, entry_date))

def get_entries():
    entries = connection.execute("SELECT * from entries;")
