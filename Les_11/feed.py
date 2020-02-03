"""
Реализовать класс, описывающий новостную ленту. 
Класс должен содержать: 
■ массив новостей; 
■ get-свойство, которое возвращает количество новостей; 
■ метод для вывода на экран всех новостей; 
■ метод для добавления новости; 
■ метод для удаления новости; 
■ метод для сортировки новостей по дате (от последних новостей до старых); 
■ метод для поиска новостей по тегу (возвращает массив новостей, в которых указан переданный в метод тег). 

Продемонстрировать работу написанных методов.
"""


from news import *
from datetime import datetime


class Feed:
    
    def __init__(self, *news):
        self.news = list(news)
        self.search_tags = []
        self.number_for_search_tags = 0
    
    @property
    def len_news(self):
        return len(self.news)
    
    def __str__(self):
        result = ''
        self.__sort_news()
        if self.number_for_search_tags:
            for item in self.search_tags:
                result += str(News(item[0], item[1], item[2], item[3:])) + '\n'
        else:
            for item in self.news:
                result += str(News(item[0], item[1], item[2], item[3:])) + '\n'
        return result
    
    def __sort_news(self):
        return self.news.sort(key=lambda d: datetime.strptime(d[2], '%d.%m.%Y'), reverse=True)
    
    def add_news(self, append_news):
        for line in self.news:
            if append_news == line:
                return False
        return self.news.append(append_news)
    
    # TODO: Добавить к списку новостей id.
    def del_news(self, name_news):
        pass
    
    def tag_news(self, tag):
        self.number_for_search_tags = 1
        self.search_tags = []
        for news in self.news:
            list_tags = []
            list_tags.extend(news[3:])
            for item in news[3:]:
                list_tags.append(item.lower())
            if tag.lower() in list_tags:
                self.search_tags.append(news)
        return self.search_tags


# TODO: Вынести список новостей в файл
news1 = ['Ливерпуль', 'Невероятный сезон Ливерпуля', '30.01.2020', 'футбол', 'Ливерпуль']
news2 = ['Apple', 'Apple обрушила цены на Iphone XS', '24.01.2020', 'технологии', 'apple']
news3 = ['Man United', 'Man United объявил о подписании Бруну Фернандеша', '28.01.2020', 'футбол', 'Man United']
news4 = ['Погода', 'В Украину идет аномальная погода', '27.01.2020', 'погода', 'Украина']
news5 = ['Google', 'Google объединит почту и мессенджер в одном приложении', '28.01.2020', 'технологии', 'Google']

news = Feed(news1, news2, news3, news4, news5)

while True:
    choice = int(input('Выберите действие: \n1 - Посмотреть новости\n2 - Добавить новость\n3 - Удалить новость\n4 - Поиск по тегу\n5 - Выход\n------> '))
    if choice == 1:
        news.number_for_search_tags = 0
        print(news)
    elif choice == 2:
        header = input('Введите название новости: ')
        text = input('Введите текст: ')
        date = input('Введите дату в формате дд.мм.гггг: ')
        tags = input('Введите теги: ')
        new_news = [header, text, date, tags]
        if news.add_news(new_news):
            print('\nУспешно добавлена\n')
        else:
            print('\nНовость уже есть в ленте\n')
    elif choice == 3:
        break
        name_news = input('Введите название новости: ')
        news.del_news(name_news)
        print('Успешно удалена')
    elif choice == 4:
        tag = input('Введите тег: ')
        if news.tag_news(tag):
            print(news)
        else:
            print('\nНовость отсутствует\n')
    else:
        break
