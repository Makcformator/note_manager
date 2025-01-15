created_date = input('Введите сегодняшнюю дату в формате "дд.мм.гггг: ')  # дата создания заметки
issue_date = input('Введите срок даты в формате "дд.мм.гггг: ')  # дата истечения заметки
title = input('Заголовок заметки: ')
text = input('Описание: ')
print(f'Дата: {created_date [0:5]}')
print(f'Срок: {issue_date [0:5]}')
print(title)
print(text)
