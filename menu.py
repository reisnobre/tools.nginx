"""."""
from __future__ import print_function, unicode_literals

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt


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
        # 'qmark': '😃',
        'message': 'Deployment',
        'name': 'deployment',
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
pprint(answers)
