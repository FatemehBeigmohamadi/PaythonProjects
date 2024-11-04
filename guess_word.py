import random

names = ['Sara', 'Alex' , 'Mary' , 'Benita' , 'Flora' , 'Ashkan']
selected_word = random.choice(names).lower()
guess_count = len(selected_word)
guess_list = ['-'] * len(selected_word)
current_guess = ' '.join(guess_list)
print(current_guess)

while guess_count>0:
    guess_char = input('enter a character: ')
    if guess_char.isalpha():
        if guess_char in selected_word:
            if guess_char in guess_list:
                print('you have guessed before! Try new character...')
            else:
                for idx , char in enumerate(selected_word):
                    if char == guess_char:
                        guess_list[idx] = guess_char
                current_guess = ' '.join(guess_list)
                print(f'Perfect ... {current_guess}')

                if not '-' in guess_list:
                    print('wooooon!')
                    break
        else:
            guess_count -= 1
            print(f'Sorry! this character is wrong... remained guesses {guess_count}')
    else:
        print('Enter valid character...')
