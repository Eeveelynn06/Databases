lName = "Library-Database"

def File(database):
    match database:
        case 1:
            return "Library-Database.txt"
        case 2:
            return "Loaner-Database.txt"
        case _:
            return SyntaxError

#Add a new book
def append(string, file):
    lName = File(file)
    with open(lName, "a") as a:
        a.write("\n" + string)

#Correct a book input (availability typically)
def overwrite(string, line, file):
    lName = File(file)
    with open(lName, "w") as w:
        w.seek(line)
        w.write(string)

#Read entire database
def read(file):
    lName = File(file)
    with open(lName, "r") as r:
        lines_list = r.readlines()
    x = 0
    while x <= len(lines_list) - 1:
        print(lines_list[x])
        x += 1

#read a specific line
def readLine(line, file):
    lName = File(file)
    with open(lName, "r") as r:
            lines_list = r.readlines()
    print(lines_list[line])


#Find a book without knowing where it is
#Find using a term
def find(searchTerm, file):
    lName = File(file)
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
    lName = File(file)
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
        budge(nameLine, 1)
        with open(lName, "w") as aIG:
            aIG.seek(nameLine)
            aIG.write(Name + " , " +  Author + " , " + ISBN + " , " + Genre + " , " + Available)
    else:
        append(Name + " , " +  Author + " , " + ISBN + " , " + Genre + " , " + Available)

#Move list down one index, starting from point
def budge(fromIndex, file):
    lName = File(file)
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

#Add a new student to a books waitlist
def Waitlist(bookIndex, newStudentIndex):
    lname = File("Library-Database.txt")
    sname = File("Student-Database.txt")
    with open(lname, "r+w") as f:
        book = f.seek(bookIndex)


def FindStudentID(studentIndex):
    studentID = ""
    lname = File("Student-Database.txt")
    with open(lname, "r") as f:
        student = f.seek(studentIndex, 0)
        for char in student:
            if char == ",":
                break
            else:
                studentID = studentID + char
            break
        return studentID