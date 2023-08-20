# Library-Management-Python
For this project, I was able to create a library management system where there are three users that have access to a database containing books. Each user has a:
1. Name
2. Id
3. Password
4. Status (student or teacher)
5. Fine.

Each book has a:
1. Name
2. Id
3. Category (genre)
4. Person id (the user that currently issued the book)
5. Days of isssue (How long has the book been issued)

## Responsibilties of user
A user can do one of the following:
1. Log in
2. Terminate Program
3. Log out
4. Pass time by days
5. View the list of available books
6. Issue a book
7. Return a bbok
8. View their account details
9. Pay fine

## How to use the program
Included in the distribution folder is a .txt file containing the names and passwords of the available users, use this information to log in when openning the .exe file. Depending on the status of the user, the project will apply certain rules. For example, the return deadline for a student is 5 days, while for a teacher is 7.

## Challanges of this project
The biggest challange I had with this project was choosing which information to reveal to the user, and finding the correct data structure to represent a user, a book , and a list of books. For simplicity I have chosen a dictionary to represent them.
