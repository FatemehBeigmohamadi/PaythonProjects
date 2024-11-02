def my_calculator():
    num1 = int(input('Enter your first number: \n'))
    num2 = int(input('Enter your second number: \n'))
    operator = input('Enter your operator (+,-,*,/): \n')

    if operator == '+':
        result = num1+num2
        print(f'num1 + num2 = {result}')

    elif operator == '-':
        result = num1-num2
        print(f'num1 - num2 = {result}')

    elif operator == '*':
        result = num1*num2
        print(f'num1 * num2 = {result}')

    elif operator == '/':
        result = num1/num2
        print(f'num1 / num2 = {result}')

    else:
        print('your numbers or operator is not correct!')

my_calculator()    
