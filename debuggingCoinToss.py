import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower() # Converts to lowercase for consistency

# Converts guess to integer for comparison
guess = 1 if guess == 'heads' else 0
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Input validation for second guess
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input().lower()

    # Converts second guess to integer
    guess = 1 if guess == 'heads' else 0
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
