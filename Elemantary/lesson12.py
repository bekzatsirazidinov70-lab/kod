# # m = {
# #     'название':'кыргыз кинолору',
# #     'год выпуска': 2021,
# #     'режисер':'аскат сулайманов',
# #     'главный актер':'аскат сулайманов'
# # }
# # m(input('название'))
# # print(m['год выпуска'])
# # print(m['режисер'])
# # print(m['главный актер'])
# #
#
#
#
#
#
# name = {
#     'name':'Asan',
#     'age': 21,
#
# }
# info = {
#     'name':''asan'
# }
# # print(name.pop('name'))
# # print(name)
#
# # name.popitem()
# # print(name)
# #
# # print(name.keys())
#
#
# # print(name.values())
# # print(name.get('name'))
# # print(name.items())
# # name.setdefault('helo','ali')
# # print(name)
from markdown_it.rules_core import block

#


num = [2, 3, 4, 5, 6, 7, 8, 9]

for start in range(0, len(num), 4):
    block = num[start:start+4]
    for i in range(2, 10):
        line = ""
        for n in block:
            line += f"{n} x {i} = {n*i:<4}  "
        print(line)
    print()


#
#
