# --------
#   Note
# --------
# and, or, not
# <, >, <=, >= , ==, !=


# # and , or
has_good_credit = False
has_good_income = True
if has_good_credit and has_good_income:
    print('you can get a lone')
else:
    print('you cannot get a lone')

if has_good_credit or has_good_income:
    print('you can get a lone')
else:
    print('you cannot get a lone')

# # not
has_criminal_record = False
if not has_criminal_record:
    print('You do not have criminal record')
    print('you can get a lone')
else:
    print('You has criminal record')
    print('you cannot get a lone')

has_good_credit = True
if not has_criminal_record and has_good_credit:
    print('You do not have criminal record and has good credit')
    print('you can get a lone')
else:
    print('You has criminal record or low credit value')
    print('you cannot get a lone')

# # >, < , ==, !=, >=, <=
temperature = 40
if temperature > 30:
    print('it is a hot day')
elif temperature < 10:
    print('it is a cold day')
else:
    print('it is not hor nor cold')

# ------- exercise -------
user_name = input('Type your user name : ')
name_length = len(user_name)
print(f"your name length is {name_length}")

if name_length < 3:
    print('user name should has at least 3 character')
elif name_length > 30:
    print('user name is too long. should less than 30 characters')
else:
    print('Name looks good')
