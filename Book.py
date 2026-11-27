books = {}


def SeperateEntries(bookIndex, startEntry):
    startChar = 0
    wantedEntry = ""
    with open("Library-Database.txt", "r") as f:
        for i, line in enumerate(f):
            if i == bookIndex:
                for char in line:
                    if startChar == startEntry:
                        if char != ",":
                            wantedEntry = wantedEntry+char
                        else:
                            return(wantedEntry)
                    elif char == ",":
                        startChar += 1

def initialize():
    with open("Library-Database.txt", "r") as f:
        for i, line in enumerate(f):
            name = SeperateEntries(i, 0)
            author = SeperateEntries(i, 1)
            isbn = SeperateEntries(i, 2)
            genre = SeperateEntries(i,3)
            available = SeperateEntries(i, 4)
            
            books[name] = {("Author",author),("iSBN",isbn),("Genre",genre),("Available",available)}


