# --------
#   Note
# --------
#
car_stopped = True
while True:
    user_input = input('> ').lower()

    if user_input == 'help':
        print('start - to start car')
        print('stop - to stop car')
        print('quit - to quit game')

    elif user_input == 'start':
        if car_stopped:
            print('Car started... Ready to go')
            car_stopped = False
        else:
            print('Car already started... ')

    elif user_input == 'stop':
        if not car_stopped:
            print('Car stopped.')
            car_stopped = True
        else:
            print('Car already stopped')

    elif user_input == 'quit':
        if car_stopped:
            print('Ok Bye')
            break
        else:
            print('You need to stop car first')

    else:
        print("I don't understand")

