# --------
#   Note
# --------
# while: else:
password = '9'
typed_count = 0
typed_limit = 3
while typed_count < typed_limit:
    user_input = input('password: ')
    typed_count += 1

    if user_input == password:
        print('Correct password')
        break
else:
    print("Sorry Incorrect password")

