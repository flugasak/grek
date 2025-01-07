# Imports
from random import choice, randint

# Functions

def get_response(user_input: str) -> str:
    #raise NotImplementedError('Cod e is missing..')
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent..'
    elif 'hello!' in lowered:
        return 'Greetings!'
    else:
        return choice([
            'I fail to comprehend',
            'Wat u on aboot?',
            'uuhh..']
        )
    
