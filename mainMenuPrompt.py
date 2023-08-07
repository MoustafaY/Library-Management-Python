from PyInquirer import prompt

def loggedInPrompt():
    choices = [
            {'name': 'Pass Time', 'value': 'pass'},
            {'name': 'View Books', 'value': 'viewBooks'},
            {'name': 'View Account Details', 'value': 'viewUser'},
            {'name': 'Issue Book', 'value': 'issue'},
            {'name': 'Return Book', 'value': 'return'},
            {'name': 'Pay Fine', 'value': 'fine'},
            {'name': 'Log Out', 'value': 'logout'}
        ]
    
    question = {
        'type': 'list',
        'name': 'action',
        'message': 'Choose your next action',
        'choices': choices
    }

    return prompt(question).get('action')

def loggedOutPrompt():
    choices = [
            {'name': 'Log In', 'value': 'login'},
            {'name': 'Terminate Program', 'value': 'terminate'}
        ]
    
    question = {
        'type': 'list',
        'name': 'action',
        'message': 'Choose your next action',
        'choices': choices
    }

    return prompt(question).get('action')