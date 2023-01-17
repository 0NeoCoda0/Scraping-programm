import json
import os
from functions import is_word_in_list
from functions import word_format
from functions import words_ending_element

database = "semantic_core.txt"
splitter = ' #'
word = ''

while True:
    with open(database, 'r', encoding='utf-8') as file:
        file_text = file.read()
        word_list = file_text.split(splitter)
    

    # ---
    # Добавить новые слова в список без повторений
    os.system('cls')
    
    list_lenght = len(word_list) - 1
    print(f'Всего в ядре {list_lenght} {words_ending_element(list_lenght)}')
    
    # вместо выражения word_format(input()) можно вставлять слова из парсинга веб-страниц
    word = word_format(input("Введите слово: "))
    while is_word_in_list(word, word_list):
        word = word_format(input("Такое уже есть в ядре. Введите другое слово: "))
    
    if word == "выход" or word == "exit":
        break
    else:
        word_list.append(word)
    # ---
    
    
    text_for_write = splitter.join(word_list)
    with open(database, 'w', encoding='utf-8') as file:
        file.write(text_for_write)
