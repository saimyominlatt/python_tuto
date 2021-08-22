# --------
#   Note
# --------
# kg <=> lbs inverter
# import math
# weight = float(input("type Your Weight: "))
#
# if math.isnan(weight):
#     print('Not a vilate weight.(weight should be number)')
#
# else:
#     unit = input("is it (L)lbs or (K)Kg: ").upper()
#     if unit == 'L':
#         print(f'{weight} lbs')
#         converted = weight / 2.2
#         print(f'{round(converted, 2)} Kg')
#
#     elif unit == 'K':
#         print(f'{weight} Kg')
#         converted = weight * 2.2
#         print(f'{round(converted, 2)} lbs')
#
#     else:
#         print('invilate input')


# ------ My Testing proj ------

# -- Myanmar length converter --

unit_names = {
    '1': 'ယူဇနာ',
    '2': 'ဂါဝုဒ်',
    '3': 'ကောသ',
    '4': 'ဥသဘ',
    '5': 'တာ',
    '6': 'တောင်',
    '7': 'ထွာ',
    '8': 'ဆုပ်',
    '9': 'လက်သစ်',
    '10': 'မုယော',
    '11': 'နှမ်း',
    '12': 'ဆံခြည်',
    '13': 'တိုင်',
    '14': 'လံ',
    '15': 'ကိုက်',
    '16': 'မိုက်',
}
values = {
    '1': 1,
    '2': 4,
    '3': 16,
    '4': 320,
    '5': 6400,
    '6': 44800,
    '7': 89600,
    '8': 179200,
    '9': 1075200,
    '10': 4300800,
    '11': 25804800,
    '12': 258048000,
    '13': 6.4,
    '14': 11200,
    '15': 22400,
    '16': 134400,
}
units_with_key = ''
for key in unit_names:
    units_with_key += f'{key}.{unit_names.get(key)} '


amount = float(input('မူလ ဂဏန်းတန်ဖိုး : '))
unit1 = input(f'မူလ ယူနစ်\n({units_with_key}): ')
unit2 = input(f'ပြောင်းလဲလိုသော ယူနစ်\n({units_with_key}): ')


def ratio():
    val_1 = values.get(unit1)
    val_2 = values.get(unit2)
    return val_2 / val_1


def converted(): return amount * ratio()


answer = f'{amount} {unit_names.get(unit1)} = {converted()} {unit_names.get(unit2)} '
print(answer)


# -  english number to Myanmar number converter
# def to_mm_num(eng_num):
#     mm_numbers = ('၀', '၁', '၂', '၃', '၄', '၅', '၆', '၇', '၈', '၉')
#     mm_num_str = ''
#     for key in str(eng_num):
#         mm_num_str += mm_numbers.__getitem__(int(key))
#     return mm_num_str
#
#
# test1 mm num converter
# num = input('num: ')
# print(to_mm_num(num))

# test2 mm num converter
# mm_num1 = int(input('mm num 1: '))
# mm_num2 = int(input('mm num 2: '))
# print(to_mm_num(mm_num1 * mm_num2))
