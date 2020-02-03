"""
Реализовать класс, описывающий новость
(заголовок, текст, массив тегов, дата публикации).
В классе необходимо реализовать один метод print,
который выводит всю информацию в таком виде:
_________________________
------ LOREM IPSUM ------
2 days ago
_________________________
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#news #article #important #hello

Обратите внимание на то, как выводится дата: 
■ если с даты публикации прошло менее дня, то выводится «сегодня»;
■ если с даты публикации прошло менее недели, то выводится «N дней назад»; 
■ в остальных случаях, полная дата в формате «дд.мм.гггг»
"""


import datetime


class News:
    
    def __init__(self, heading, text, date_news, tags):
        self.heading = heading
        self.text = text
        self.date_news = date_news
        self.tags = tags
        
    def __publication_date(self):
        list_date = [int(item) for item in self.date_news.split(".")]
        
        now = datetime.datetime.now()
        then = datetime.datetime(list_date[2], list_date[1], list_date[0])
        delta = now - then
        count_day = delta.days
        
        assert count_day >= 0, 'Некорректная дата'
        if count_day < 1:
            self.date_news = 'Today'
        elif count_day < 7:
            self.date_news = str(count_day) + ' days ago'
            if count_day == 1:
                self.date_news = str(count_day) + ' day ago'
        else:
            self.date_news = datetime.date(list_date[2], list_date[1], list_date[0]).strftime("%d.%m.%Y")
        return self.date_news
    
    def __str__(self):
        ch1 = '_'
        ch2 = '-'
        length_ch1 = len(self.heading) + (len(ch2) * 5) * 2
        # Добавляем "_"
        result = '\n' + '_' * 50 + '\n'
        result += '\t' + ch1 * length_ch1 + '\n'
        # Добавляем заголовок
        result += f'\t{self.heading.center(length_ch1, ch2)}\n'
        # Добавляем дату
        result += f'\t{self.__publication_date()}\n'
        # Добавляем "_"
        result += f'\t{ch1 * length_ch1}\n\n{self.text}\n\n\t'
        # Добавляем теги
        list_tags = ['#' + item for item in self.tags]
        result += ' '.join(list_tags) + '\n' + '_' * 50
        return result
