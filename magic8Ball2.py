import random

messages = ['It is certain',
            'It is decidely so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
while True:
    print('Ask anything...')
    user_input = input()
    if user_input == '':
        break
    else:
        print(messages[random.randint(0, len(messages) -1)])
        print()
print('Ask if you are ready.')
