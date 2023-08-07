from PyInquirer import prompt

        
def userPrompt():
    question =  {
        'type': 'input',
        'name': 'name',
        'message': 'Enter your Name:'
    }
    return prompt(question).get('name')

def passwordPrompt():
     question = {
          'type': 'input',
          'name': 'pass',
          'message': 'Enter your password:'
     }
     return prompt(question).get('pass')

def finePrompt():
    question = {
        'type': 'input',
        'name': 'amount',
        'message': 'Enter amount to fine'
    }

    return float(prompt(question).get('amount'))

def paymentPrompt():
    question = {
        'type': 'input',
        'name': 'amount',
        'message': 'Enter amount to pay'
    }

    return float(prompt(question).get('amount'))

def passTimePrompt():
     question = {
          'type': 'input',
          'name': 'time',
          'message': 'How much time do you want to pass?'
     }
     return int(prompt(question).get('time'))