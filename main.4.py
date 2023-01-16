from random import randint

try:
    a = randint(1,500)
    counter = 0
    last = 0
    while True:
            b = int(input(f'число[0 - 500: last:{last} ]:'))
            if a > b:
                print('число більше')
            elif a <b:
                print('число менше')
            else:
                print('вітаю! число вгадане.')
                break
                counter+=1
                last = b


except Exception as ex:
            print(f'Error [{ex.__class__.__name__}]: {ex}')