# entries = [
#     {"content": "Today I started learning python", "date": "2019-01-01"},
#     {"content": "I create my first database", "date": "2019-02-01"},
#     {"content": "I finished writing my programming diary app", "date": "2019-03-01"},
#     {"content": "I finished writing my prog diary today!", "date": "2019-04-01"},
#     {"content": "Today I'm continuing my learning on programming", "date": "2019-04-02"},
# ] 
import sqlite3

entries = []

try:
    connection = sqlite3.connect('.\PROGDIARY\data.db')
    print("Connection made to database.")
except:
    print("Could not connect to database.")

def create_table():
    with connection:  # uses context manager to handle commit/rollback of the transaction.
        connection.execute('CREATE TABLE entries (content TEXT, date TEXT);')

def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})

def get_entries():
    return entries
