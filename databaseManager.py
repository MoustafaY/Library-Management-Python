import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

def queryBooks(category='All'):
    if category == 'All':
        cursor.execute("""
               SELECT rowid, name, author, category FROM books
               WHERE personID is NULL
    """)
    else:
        cursor.execute("""
                SELECT rowid, name, author, category FROM books
                WHERE category = ? AND personID is NULL
    """, (category,))
    
    result = cursor.fetchall()
    
    connection.commit()

    return result


def getUser(userName, userPassword):
    cursor.execute("""
            SELECT personID, name, status, fine, Passwords FROM users
            WHERE UPPER(name) = ? AND Passwords = ?
                   
""", (userName.upper(), userPassword))
    result = cursor.fetchall()
    connection.commit()

    return result

def issueBook(userId, bookId):
    cursor.execute("""
               UPDATE books SET personID = ?
               WHERE bookID = ? AND personID is NULL
""", (userId, bookId))
    connection.commit()

    return cursor.rowcount

def returnBook(userId, bookId):
    cursor.execute("""
          UPDATE books SET personID = NULL WHERE personID = ? AND bookID = ?;    
""", (userId, bookId))
    connection.commit()
    result = cursor.rowcount

    if result != 0:
        cursor.execute("""
            UPDATE books SET daysOfIssue = ? Where bookID = ?;    
    """, (0, bookId))
        connection.commit()

    return result

def resetBooks():
    cursor.execute("""
            UPDATE books SET personID = NULL
            WHERE personID is NOT NULL
""")
    connection.commit()
    
def getUserBooks(userId):
    cursor.execute("""
            SELECT rowid, name, author, category, daysOfIssue FROM books WHERE personID = ?
""", (userId,))
    result = cursor.fetchall()
    connection.commit()
    return result


def payFine(userId, newAmount):
    cursor.execute("""
            UPDATE users SET fine = ? WHERE personID = ?
""", (newAmount, userId))
    connection.commit()

    return cursor.rowcount

def setFine():
    cursor.execute("""
            UPDATE users SET fine = ?
""", (0.0,))
    connection.commit()

def setDays():
    cursor.execute("""
            UPDATE books SET daysOfIssue = ?
""", (0,))
    connection.commit()

def passTimeForBooks(time):
    cursor.execute("""
            SELECT bookID, daysOfIssue From books WHERE personID is not NULL
    """)
    daysOfIssue = cursor.fetchall()

    for day in daysOfIssue:
        newDate = day[1] + time
        cursor.execute("""
                UPDATE books SET daysOfIssue = ? WHERE bookID = ?
            """, (newDate, day[0]))
        connection.commit()

def passTimeForUsers(time):
    cursor.execute("""
            SELECT daysOfIssue, personID FROM books WHERE personID is not NULL
""")
    books = cursor.fetchall()
    for book in books:
        dayNumber = book[0]
        userId = book[1]
        cursor.execute("""
            SELECT status, fine FROM users WHERE personID = ?
""", (userId,))
        user = cursor.fetchall()
        status = user[0][0]
        fine = user[0][1]
        if dayNumber > 7 and status == "Teacher":
            if time == dayNumber:
                fineTeacher(userId, fine, time - 7)
            else:
                fineTeacher(userId, fine, time)
        elif dayNumber > 5 and status == "Student":
            if time == dayNumber:
                fineStudent(userId, fine, time - 5)
            else:
                fineStudent(userId, fine, time)

def fineTeacher(userId, oldFine, time):
    newFine = calculateFineTeacher(oldFine, time)
    cursor.execute("""
            UPDATE users SET fine = ? WHERE personID = ?
""", (newFine, userId))
    connection.commit()

def calculateFineTeacher(oldFine, time):
    return oldFine + (5 * time)

def fineStudent(userId, oldFine, time):
    newFine = calculateFineStudent(oldFine, time)
    cursor.execute("""
            UPDATE users SET fine = ? WHERE personID = ?
""", (newFine, userId))
    connection.commit()

def calculateFineStudent(oldFine, time):
    return oldFine + (10 * time)
    
def closeConnection():
    connection.close()