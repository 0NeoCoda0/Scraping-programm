from functions import download_tag_data
from functions import clear_hyperlinks
from functions import clear_noise_to
from functions import list_format
from functions import binary_search
from functions import find_all_matches
from add_water import add_water
import os

database = "semantic_core.txt"
splitter = ' #'
# загрузить семантическое ядро
with open(database, 'r', encoding='utf-8') as file:
    file_text = file.read()
    raw_semantic_core = file_text.split(splitter)
    semantic_core = []
    for item in raw_semantic_core:
        new_item = item.replace('_', ' ')
        semantic_core.append(new_item)
    semantic_core = sorted(semantic_core)
    semantic_core.pop(0)


# получить контент со страницы
target_id = 275000
i = 273100
while i < target_id:
    os.system('cls')
    print(i)
    url = f'https://gamedev.ru/job/forum/?id={i}'
    tag = 'div'
    tag_atributes = {'class': 'bound overflow'}
    web_data = download_tag_data(url, tag, tag_atributes)

    if web_data != None and web_data != '':
        # очистить контент от шума
        noise_to_empty = ['.', ',', ':', '!', '?']
        noise_to_space = ['/', ')', '(', '-', '_']
        empty_char = ''
        space_char = ' '

        proccessed_web_data = clear_noise_to(
            noise_to_empty, web_data, empty_char)
        proccessed_web_data = clear_noise_to(
            noise_to_space, proccessed_web_data, space_char)
        proccessed_web_data = clear_hyperlinks(proccessed_web_data)

        # подготовить данные извлеченные из веб-станицы для сравнения с ядром
        proccessed_web_data = proccessed_web_data.lower()
        list_web_data = proccessed_web_data.split()
        list_web_data = list_format(list_web_data)
        web_data_prepared = sorted(list_web_data)

        # сравнить ядро и веб_текст.
        #print("\nРЕЗУЛЬТАТЫ ПАРСИНГА\n")
        number_of_matches = find_all_matches(semantic_core, web_data_prepared)

        # вычислить процентное соотношение ключевых слов в тексте.
        full_filling = len(web_data_prepared) + number_of_matches
        try:
            percentage_of_similarity = number_of_matches / full_filling * 100
        except ZeroDivisionError:
            print(f"Похоже страницы {i} не существует, проверь.")

        #print(number_of_matches, full_filling)
        #print("Данные после сравнения\n", web_data_prepared)
        #print(f'Процент соответствия {percentage_of_similarity}')
        # add_water(web_data_prepared)

        # Вернуть url ссылку, если соответствие больше 15%
        if percentage_of_similarity > 20:
            with open(f'parse_data/{i}.html', 'w', encoding='utf8') as f:
                f.write(web_data)
    i += 1

"""Поисковый алгоритм
1. Собрать семантическое ядро
2. Оправлять в поисковик различные комбинации запросов
3. Анализировать количество найденных страниц
4. Сортировать результаты комбинаций в порядке возрастания
5. Предоставлять список всех найденных ссылок
6. Анализировать ссылки по семантическому ядру
7. Предоставлять список ссылок с уровнем соответствия больше 60%
8. Сортировать по дате изменения

"""
