status = {'Ваш статус': 'В процессе'}
def restatus(status):
    print(status)
    x = int(input("Можете изменить на: \n"
                      "1 - Выполнено\n"
                      "2 - В процессе\n"
                      "3 - Отложено\n"))
    if x == 1:
            return ('Выполнено')
    elif x == 2:
            return ('В процессе')
    elif x == 3:
            return ('Отложено')
    else:
            return ('Ввели не правильный формат')
status['Ваш статус'] = restatus(status)
print(status)