import numpy as np
import matplotlib as plt 

a=np.array(['Мцыри', 'Преступление и наказание', 'Кортик', 'Бородино', 'Молодая гвардия', 'Евгений Онегин', 'Герой нашего времени', 'Идиот', 'Зойкина квартира', 'Демон', 'Собачье Сердце', 'Сборник романов Достоевского', 'Стихотворения Лермонтова', 'Белая гвардия', 'Мастер и Маргарита', 'Лучшие произведения М.Ю. Лермонтова', 'Горячий снег', 'Дикая собака Динго', 'Беглец', 'Стихотворения Пушкина', 'Василий Теркин', 'Выхожу один я на дорогу', 'Война и Мир', 'Анна Каренина', 'Кинжал',
         'Севастопольские рассказы', 'Бал', 'Ангел', 'Романы Толстого', 'Князь Серебряный','Сердца Трех','По Ком Звонит Колокол', 'Марк Твен', 'Малыш и Карлсон', 'Великий Гетсби', 'Маугли',
         'Мио, Мой Мио', 'На западном фронте без перемен', 'Портрет Дориана Грея', 'Мартин Иден', 'Собор Парижской Богоматери', 'Отверженные', 'Белый Клык', 'Человек, который смеется', 'Детективы Агаты Кристи',
         'Фауст', 'Лучшие стихотворения Киплинга', 'Рубаи Омара Хайяма', 'Сонеты Уильяма Шекспира', 'Гомер: Иллиада', 'Гомер: Одиссея', 'Ворон', 'Уильям Блейк',
         'Гораций', 'Басё', 'Сборник стихотворений Гёте', 'Шиллер. Избраннные произведения', 'Сайгё', 'Сборник Роберта Бернса', 'Омар Хайям'])


#print(a,len(a))

b= a[a.size//2:3*a.size//4:3]
print(b)

