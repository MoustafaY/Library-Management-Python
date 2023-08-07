from PyInquirer import prompt

def categoryPrompt():
    choices = [
        {'name': 'Horror', 'value': 'Horror'},
        {'name': 'Adventure', 'Value': 'Adventure'},
        {'name': 'All', 'Value': 'All'}
    ]
    question = {
        'type': 'list',
        'name': 'category',
        'message': 'Which category of books are you looking for?',
        'choices': choices
    } 

    return prompt(question).get('category')

def bookPrompt():
    question = {
        'type': 'input',
        'name': 'id',
        'message': 'Enter book ID (0 to go back):'
    }
    return prompt(question).get('id')