birthdays = {'Alice': 'Apr 1',
            'Bob': 'Dec 12',
            'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info for ' + name)
        print('What is their birthday?')
        birthday = input()
        birthdays[name] = birthday
        print('Birthday database updated.')
    
