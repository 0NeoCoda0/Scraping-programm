from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def binary_search(target: str, text_list: list) -> int:
    low_index = 0
    high_index = len(text_list) - 1

    while low_index <= high_index:
        mid_index = int((low_index + high_index) / 2)
        if target == text_list[mid_index]:
            return mid_index
        if target < text_list[mid_index]:
            high_index -= 1
        else:
            low_index += 1
    return None


def is_word_in_list(word: str, list: list) -> bool:
    if word in list:
        return True
    else:
        return False


def list_format(list: list[str]) -> list:
    database = "water_words.txt"
    splitter = ' #'
    new_list = []
    new_item = ''

    for item in list:
        new_item = item.replace('-', ' ').replace('_', ' ').replace('\"','').replace(';','').replace('\'','')
        new_list.append(new_item)

    with open(database, 'r', encoding='utf-8') as file:
        file_text = file.read()
        water_list = file_text.split(splitter)

    water_list = [' ','-'] + water_list
    set_water_list = frozenset(water_list)
    cleared_list = [item for item in new_list if item not in set_water_list]
    return cleared_list


def word_format(word: str) -> str:
    word = word.lower()
    word = word.replace(' ', '_').replace('-', '_')
    return word


def words_ending_element(number: int) -> str:
    item = str(number)
    str_lenght = len(item) - 1

    teen = ['11', '12', '13', '14', '15', '16', '17', '18', '19']
    on_5_to_9 = ['5', '6', '7', '8', '9']

    is_teen = item[str_lenght - 1:] in teen
    is_5_to_9 = item[str_lenght:] in on_5_to_9
    is_zero = item[-1] == '0'

    if is_teen or is_5_to_9 or is_zero:
        return 'элементов'

    elif item[-1] == '1':
        return 'элемент'
    elif item[-1] == '2':
        return 'элемента'
    elif item[-1] == '3':
        return 'элемента'
    elif item[-1] == '4':
        return 'элемента'


def clear_noise_to(noise_list: list, target_string: str, target_char: str) -> str:
    old_text_list = target_string.split()
    new_text_list = []

    for item in old_text_list:
        is_cleared = False
        for noise_char in noise_list:
            if noise_char in item:
                item = item.replace(noise_char, target_char)
                is_cleared = True
                new_item = item
        if is_cleared:
            new_text_list.append(new_item)
        else:
            new_text_list.append(item)

    return ' '.join(new_text_list)


def clear_hyperlinks(text: str) -> str:
    # очистить текст от гиперссылок
    start = text.find('<a')
    end = text.find('</a>')
    if start != -1:
        while end != -1:
            text = text[:start] + text[end + 1:]
            end = text.find('</a>')
    return text


def download_tag_data(url: str, tag: str, atributes: dict):
    text_content = ''
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html5lib')
    except HTTPError:
        print('Страницы не существует или была удалена')
    try:
        web_html_content = bs.body.find_all(tag, atributes)
        for item in web_html_content:
            text_content += item.get_text()
        return text_content
    except AttributeError as error:
        print(error)


def find_all_matches(semantic_core, prepared_data):
    counter = 0
    for item in semantic_core:
        finding_index = binary_search(item, prepared_data)
        if finding_index != None:
            print(prepared_data[finding_index])
            prepared_data.pop(finding_index)
            counter += 1
            counter += find_all_matches(semantic_core, prepared_data)
    return counter
