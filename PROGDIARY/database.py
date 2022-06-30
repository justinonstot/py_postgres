entries = [
    {"content": "Today I started learning python", "date": "2019-01-01"},
    {"content": "I create my first database", "date": "2019-02-01"},
    {"content": "I finished writing my programming diary app", "date": "2019-03-01"},
    {"content": "I finished writing my prog diary today!", "date": "2019-04-01"},
    {"content": "Today I'm continuing my learning on programming", "date": "2019-04-02"},
] 


def add_entry(entry_content, entry_date):
    # entry_content = input("What have you learned today? ")
    # entry_date = input("Enter the date (YYYY-MM-DD: ")
    entries.append({"content": entry_content, "date": entry_date})

def get_entries():
    return entries
