# --------
#   Note
# --------
# if, else
# if, elif, else

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Stay warm")
else:
    print("It is a Lovely day")

print('Enjoy your day')

# ----- exercise -----
price = 1000000
is_good_credit = False
if is_good_credit:
    print('You has good credit')
    print(f'Price for you is only : ${price*.9}')
else:
    print('You do not have good credit')
    print(f'Price for you is only : ${price}')
