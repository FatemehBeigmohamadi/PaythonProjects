import random
try:
    low = int(input('Please enter lower bound: \n'))
    high = int(input('Please enter lower bound: \n'))
except:
    print('Enter a valid value...')

r = random.randint(low,high)
guess_count = 5
while guess_count>0:
    try:
        print (f'you can {guess_count} time to guess number.')
        user_guess = int(input('Enter your guess number: \n'))
        if user_guess == r:
            print('Greet! you guess True!')
            break
        elif user_guess < r:
            print('your guess is lower than selected number. ')
        else:
            print('your guess is higher than selected number. ')
        
        guess_count -=1
        print('*'*50)
    except:
        print('Enter a valid value...')
