'''
while->без конечно иштей ала турган цикл
'''

# while 20 > 10:
#     print(20*2)

# num = 0
# while num <=10:
#     print( num,'Bekzat')
#     num +=1


'''
break->токтотуу (токтотуу)
continue -> улантуу (аттап отуу)
'''


# кортеж типы данных



while True:
    num = input('Введите пароль')
    if len(num) < 8:
        print('короткий')
        continue
    num1 = False
    for str in num:
        if str.isdigit():
                num1 = True
                break
    if not num1:
        print('нет цифр')
        continue
    num2 = False
    for str in num:
        if str.isalpha():
            num2 = True
            break
    if not num2:
        print('нет буквы')
        continue
    num3 = False
    for str in num:
        if not str.isdigit()or str.isalpha():
            num3 = True
        break
    if not num3:
        print('нет символов')
        continue
    else:
        print('успешно')
        break
