value = 1
def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

print('Enter number:')
for guess in range(10):
    try:
        userInput = collatz(int(input()))
        if userInput == value:
            break
            
    except ValueError:
        print('Please enter a valid integer.')
if userInput == value:
    pass
else:
    print('idiot')
