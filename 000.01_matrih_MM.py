# -- Myanmar length converter --

# mm_unit_names = {
#     '1': 'ယူဇနာ',
#     '2': 'ဂါဝုဒ်',
#     '3': 'ကောသ',
#     '4': 'ဥသဘ',
#     '5': 'တာ',
#     '6': 'တောင်',
#     '7': 'ထွာ',
#     '8': 'ဆုပ်',
#     '9': 'လက်သစ်',
#     '10': 'မုယော',
#     '11': 'နှမ်း',
#     '12': 'ဆံခြည်',
#     '13': 'တိုင်',
#     '14': 'လံ',
#     '15': 'ကိုက်',
#     '16': 'မိုက်',
# }
# mm_values = {
#     '1': 1,
#     '2': 4,
#     '3': 16,
#     '4': 320,
#     '5': 6400,
#     '6': 44800,
#     '7': 89600,
#     '8': 179200,
#     '9': 1075200,
#     '10': 4300800,
#     '11': 25804800,
#     '12': 258048000,
#     '13': 6.4,
#     '14': 11200,
#     '15': 22400,
#     '16': 134400,
# }
# mm_units_with_key = ''
# for key in mm_unit_names:
#     mm_units_with_key += f'{key}.{mm_unit_names.get(key)} '
#
#
# amount = float(input('မူလ ဂဏန်းတန်ဖိုး : '))
# unit1 = input(f'မူလ ယူနစ်\n({mm_units_with_key}): ')
# unit2 = input(f'ပြောင်းလဲလိုသော ယူနစ်\n({mm_units_with_key}): ')
#
#
# def ratio():
#     val_1 = mm_values.get(unit1)
#     val_2 = mm_values.get(unit2)
#     return val_2 / val_1
#
#
# def converted(): return amount * ratio()
#
#
# answer = f'{amount} {mm_unit_names.get(unit1)} = {converted()} {mm_unit_names.get(unit2)} '
# print(answer)

mt_unit_names = {
    '1': 'League',
    '2': 'mile',
    '3': 'furlong',
    '4': 'rod',
    '5': 'yard',
    '6': 'foot',
    '7': 'inch',
}
mt_values = {
    '1': 1,
    '2': 3,
    '3': 16,
    '4': 320,
    '5': 6400,
    '6': 44800,
    '7': 89600,
}
mt_units_with_key = ''
for key in mt_unit_names:
    mt_units_with_key += f'{key}.{mt_unit_names.get(key)} '


amount = float(input('မူလ ဂဏန်းတန်ဖိုး : '))
unit1 = input(f'မူလ ယူနစ်\n({mt_units_with_key}): ')
unit2 = input(f'ပြောင်းလဲလိုသော ယူနစ်\n({mt_units_with_key}): ')


def ratio():
    val_1 = mt_values.get(unit1)
    val_2 = mt_values.get(unit2)
    return val_2 / val_1


def converted(): return amount * ratio()


answer = f'{amount} {mt_unit_names.get(unit1)} = {converted()} {mt_unit_names.get(unit2)} '
print(answer)


