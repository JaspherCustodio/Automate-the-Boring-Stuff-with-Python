cat_names = []
while True:
    print('Enter the name of cat '
          + str(len(cat_names) + 1)
    + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # List concatenation.

while True:
    print('Enter a cat name.')
    name = input()
    if name == '':
        break
    elif name == 'dog':
        print("I don't have " + name)
    elif name not in cat_names:
        print('I do not have a cat named ' + name)
    else:
        print(name + ' is my cat.')

    

print('The cat names are:')
for name in cat_names:
    print(' ' + name)
