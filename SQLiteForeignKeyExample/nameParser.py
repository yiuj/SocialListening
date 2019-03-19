import sqlite3

def main():
    input = open("input.txt", "r")
    nameList = []

    for line in input:
        words = line.split()
        for word in words:
            email = False
            period = False
            for i in range(0, len(word)):
                if word[i] == '@':
                    email = True
                if word[i] == '.':
                    period = True
            if email and period:
                name = findName(word)
                nameList.append(name)

    for name in nameList:
        print(name)

    mydb =sqlite3.connect("emailDB.db")
    c = mydb.cursor()

    # c.execute("CREATE TABLE User("
    #           "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"
    #           "name TEXT,"
    #           "email TEXT)")
    # c.execute("CREATE TABLE Course("
    #           "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"
    #           "title TEXT)")
    # c.execute("CREATE TABLE Member("
    #           "user_id INTEGER,"
    #           "course_id INTEGER,"
    #           "PRIMARY KEY (user_id, course_id))")

    # c.execute("INSERT INTO User(name, email) VALUES ('William', 'masdon@usc.edu'),('James', 'james@usc.edu')")
    # c.execute("INSERT INTO Course (title) VALUES ('Python')")

    # c.execute("INSERT INTO Member (user_id, course_id) VALUES (1, 1),(2,1)")

    c.execute("SELECT User.name, User.email, Course.title FROM User JOIN Member JOIN Course ON Member.user_id = User.id AND Member.course_id = Course.id")

    print(c.fetchall())


    mydb.commit()





def findName(email):
    name = email.split('@')
    if name[0][0] == "<":
        return name[0][1:]
    else:
        return name[0]


main()