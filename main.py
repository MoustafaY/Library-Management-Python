import databaseManager as db
from prettytable import PrettyTable
import userPrompts as userP
import bookPrompts as bookP
import mainMenuPrompt as mainMenuP

def printBooks():
    category = bookP.categoryPrompt()
    table = getBooksByCategory(category)
    print(table)

def getBooksByCategory(category):
    result = db.queryBooks(category)

    columnNames = ['Book ID', 'Book Name', 'Book Author', 'Book Category']

    table = PrettyTable(columnNames)

    for row in result:
        table.add_row(row)
    
    return table


def login():
    user = getUser()
    return user


def getUser():
    found = False
    while found is False:
        userName = userP.userPrompt()
        userPassword = userP.passwordPrompt()
        userQuery = db.getUser(userName, userPassword)
        found = checkLengthOfQuery(userQuery)
    
    user = formatQuery(userQuery)
    return user

def formatQuery(user):
    return {'id': user[0][0], 'name': user[0][1], 'status': user[0][2], 'fine': user[0][3], 'password': user[0][4]}

def checkLengthOfQuery(query):
    if len(query) != 0:
        return True
    print("Invalid input")
    return False

def issueBook(userId):
    while True:
        bookId = bookP.bookPrompt()
        if int(bookId) == 0:
            return
        result = db.issueBook(userId, bookId)
        if result != 0:
            break
        print("Invalid id")


def returnBook(userId):
    print("Your issued books:")
    printUserBooks(userId)
    while True:
        bookId = bookP.bookPrompt()
        if int(bookId) == 0:
            return
        result = db.returnBook(userId, bookId)
        if result != 0:
            break
        print("Invalid id")


def printUserBooks(userId):
    result = db.getUserBooks(userId)

    columnNames = ['Book ID', 'Book Name', 'Book Author', 'Book Category', 'Days of Issue']

    table = PrettyTable(columnNames)

    for row in result:
        table.add_row(row)
    
    print(table)
      

def printUser(user):
    tupleUser = (user.get('id'), user.get('name'), user.get('status'), user.get('fine'))

    columnNames = ['ID', 'Name', 'Status', 'Fine']
    table = PrettyTable(columnNames)

    table.add_row(tupleUser)
    print(table)


def payFine(user):
    while True:
        amount = userP.paymentPrompt()
        if amount <= user.get('fine'):
            break
        print("Invalid payment amount")
    newFine = calculateForPayment(amount, user.get('fine'))
    db.payFine(user.get('id'), newFine)


def calculateForPayment(amount, fine):
    return fine - amount

def updateUser(user):
    result = db.getUser(user.get('name'), user.get('password'))
    formattedUser = formatQuery(result)
    return formattedUser

def loggedOutMenu():
    action = mainMenuP.loggedOutPrompt()
    if action == "login":
        return login()
    else:
        return False

def loggedInMenu(user):
    action = mainMenuP.loggedInPrompt()
    if action == "pass":
        time = userP.passTimePrompt()
        passTime(time)
    elif action == "viewUser":
        printUser(user)
    elif action == "viewBooks":
        printBooks()
    elif action == "issue":
        issueBook(user.get('id'))
    elif action == "return":
        returnBook(user.get('id'))
    elif action == "fine":
        payFine(user)
    elif action == "logout":
        return False
    return True

def passTime(time):
    db.passTimeForBooks(time)
    db.passTimeForUsers(time)
    print("Time passed by {} day(s)".format(time))



def main():
    user = loggedOutMenu()
    if user is False:
        print("Goodbye!")
        return
    flag = True
    while True:
        if flag is False:
            user = loggedOutMenu()
            if user is False:
                print("Goodbye!")
                break
            flag = True
        else:
            flag = loggedInMenu(user) 
            user = updateUser(user) 
    db.closeConnection()



if __name__ == "__main__":
    main()