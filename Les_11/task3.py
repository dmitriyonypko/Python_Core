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


from datetime import datetime


class Feed:

    def __init__(self, *news):
        self.news = list(news)

    @property
    def len_news(self):
        return len(self.news)

    def print_news(self):
        for item in self.news:
            print(', '.join(item) + '\n')

    def add_news(self, append_news):
        return self.news.append(append_news)

    def del_news(self):
        name_news = input("Введите новость которую хотите удалить: ").split(', ')
        return self.news.remove(name_news)

    def sort_news(self):
        return self.news.sort(key=lambda d: datetime.strptime(d[1], '%d.%m.%Y'), reverse=True)

    def tag_news(self, tag):
        for news in self.news:
            if tag == news[2]:
                print(', '.join(news) + '\n')


news1 = ['Невероятный сезон Ливерпуля', '30.01.2020', 'футбол']
news2 = ['Apple обрушила цены на Iphone XS', '24.01.2020', 'технологии']
news3 = ['МЮ объявил о подписании Бруну Фернандеша', '28.01.2020', 'футбол']
news4 = ['В Украину идет аномальная погода', '27.01.2020', 'погода']
news5 = ['Google объединит почту и мессенджер в одном приложении', '28.01.2020', 'технологии']

new_news = ['В Украине пропала мобильная связь "Киевстар"','31.01.2020','связь']
tag = 'технологии'


news = Feed(news1, news2, news3, news4, news5)


news.print_news()

print('_' * 100)
news.add_news(new_news)
news.print_news()

print('_' * 100)
news.del_news()
news.print_news()

print('_' * 100)
news.sort_news()
news.print_news()

print('_' * 100)
news.tag_news(tag)

