import json
with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(data['welcome'])
while True:
    prompt(data['first'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['invalid'])
        number1 = input()

    prompt(data['second'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['invalid'])
        number2 = input()


    prompt(data['operation'])

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data['invalid op'])
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output= int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f"{data['result']} {output}")
    
    prompt(data['continue'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
