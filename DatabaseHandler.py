lName = ""

def file(database):
    match database:
        case 1:
            return "Library-Database.txt"
        case 2:
            return "Loaner-Database.txt"
        case _:
            return SyntaxError

#Add a new book
def append(string, file):
    lName = file(file)
    with open(lName, "a") as a:
        a.write("\n" + string)

#Correct a book input (availability)
def overwrite(string, line, file):
    lName = file(file)
    with open(lName, "w") as w:
        w.seek(line)
        w.write(string)

#Read entire database
def read(file):
    lName = file(file)
    with open(lName, "r") as r:
        lines_list = r.readlines()
    x = 0
    while x <= len(lines_list) - 1:
        print(lines_list[x])
        x += 1

#read a specific line
def readLine(line, file):
    lName = file(file)
    with open(lName, "r") as r:
            lines_list = r.readlines()
    print(lines_list[line])


#Find a book without knowing where it is
#Find using a term
def find(searchTerm, file):
    lName = file(file)
    with open(lName,"r") as f:
        lines_list = f.readlines()
    x = 0
    while x != len(lines_list):
        if searchTerm in lines_list[x]:
            print(lines_list[x])
        x += 1

#Add a book in the middle of the database
#For the case of adding to Genre
def add(Name, Author, ISBN, Genre, Available, file):
    lName = file(file)
    with open(lName, "r") as aIG:
        lines_list = aIG.readlines()
    x = 0
    genreLine = 0
    authorLine = 0
    nameLine = 0
    while x < len(lines_list):
        if Genre in lines_list[x]:
            genreLine = x
            break
        x += 1
    while genreLine < len(lines_list):
        if Author in lines_list[genreLine]:
            authorLine = genreLine
            break
        else:
            genreLine += 1
    while authorLine < len(lines_list):
        if Name in lines_list[authorLine]:
            nameLine = authorLine
            break
        authorLine += 1
    if nameLine != 0:
        budge(nameLine)
        with open(lName, "w") as aIG:
            aIG.seek(nameLine)
            aIG.write(Name + " , " +  Author + " , " + ISBN + " , " + Genre + " , " + Available)
    else:
        append(Name + " , " +  Author + " , " + ISBN + " , " + Genre + " , " + Available)

#Move list down one index, starting from point
def budge(fromIndex, file):
    lName = file(file)
    with open(lName, "r") as f:
        lines_list_orig = f.readlines()
        f.seek(0)
        lines_list = f.readlines()
        lines_list.append("0")
        i = 0
        while i<=len(lines_list_orig):
            lines_list[fromIndex + 1] = lines_list_orig    
            pass
    with open(lName, "w") as f:
        f.writelines(lines_list)