import random
import time

def question_generator():
    a = random.randint(1,9)
    b = random.randint(1,9)
    operator_list = ['+' , '-' , '*' , '/']
    selcted_operator = random.choice(operator_list)
    print(f'{a} {selcted_operator} {b} = ?')
    
    if selcted_operator == '+':
        return a + b
    elif selcted_operator == '-':
        return a - b
    elif selcted_operator == '*':
        return a * b
    else:
        return a/b

question_number_limit = 5
question_number = 0
score = 0
time_limit = 10

while question_number < question_number_limit:

    start_time = time.time()
    result = str(question_generator())
    user_answer = input('Enter youe answer: ')
    end_time = time.time()

    time_dif = end_time - start_time

    if time_dif <= time_limit :

        if user_answer == result:
            score += 1
            print(f'correct! your score is {score} .')
        else:
            print('Sorry! your answer is wrong...')
    else:
        print('Sorry! your time finished...')

    question_number += 1
    
print(f'Final score is {score} out of {question_number}')