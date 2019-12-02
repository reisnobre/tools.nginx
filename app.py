"""."""

from __future__ import print_function, unicode_literals
# from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt

from classes.deployment import Deployment


STYLE = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


QUESTIONS = [
    {
        'type': 'input',
        'message': 'Domain ?',
        'name': 'domain',
        'default': 'mysite.com'
    },
    {
        'type': 'list',
        'message': 'Deployment',
        'name': 'target',
        'choices': [
            {
                'name': 'laravel'
            },
            {
                'name': 'vue'
            },
            {
                'name': 'wordpress'
            }
        ]
    }
]

answers = prompt(QUESTIONS, style=STYLE)

deployment = Deployment(answers['target'], answers['domain'])
deployment.clear()
deployment.create()
deployment.setup()
# deployment.clear()
