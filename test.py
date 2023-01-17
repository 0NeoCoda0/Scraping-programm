import unittest
from functions import is_word_in_list
from functions import words_ending_element
from functions import binary_search
from functions import clear_hyperlinks
from functions import clear_noise_to
from functions import find_all_matches


class FunctionTesting(unittest.TestCase):

    def test_is_word_in_list(self):
        list = ['buggy', 'muggy', 'sluggy']
        word = 'buggy'
        word_2 = 'defcon'
        self.assertEqual(is_word_in_list(word, list), True)
        self.assertEqual(is_word_in_list(word_2, list), False)

    def test_words_ending_element(self):
        self.assertEqual(words_ending_element(0), 'элементов')
        self.assertEqual(words_ending_element(1), 'элемент')
        self.assertEqual(words_ending_element(2), 'элемента')
        self.assertEqual(words_ending_element(3), 'элемента')
        self.assertEqual(words_ending_element(4), 'элемента')
        self.assertEqual(words_ending_element(5), 'элементов')
        self.assertEqual(words_ending_element(6), 'элементов')
        self.assertEqual(words_ending_element(7), 'элементов')
        self.assertEqual(words_ending_element(8), 'элементов')
        self.assertEqual(words_ending_element(9), 'элементов')
        self.assertEqual(words_ending_element(10), 'элементов')
        self.assertEqual(words_ending_element(6411), 'элементов')
        self.assertEqual(words_ending_element(13), 'элементов')
        self.assertEqual(words_ending_element(2312), 'элементов')
        self.assertEqual(words_ending_element(21), 'элемент')
        self.assertEqual(words_ending_element(32), 'элемента')
        self.assertEqual(words_ending_element(43), 'элемента')
        self.assertEqual(words_ending_element(54), 'элемента')
        self.assertEqual(words_ending_element(101), 'элемент')
        self.assertEqual(words_ending_element(202), 'элемента')
        self.assertEqual(words_ending_element(314), 'элементов')
        self.assertEqual(words_ending_element(543621), 'элемент')
        self.assertEqual(words_ending_element(53213), 'элементов')

    def test_clear_hyperlinks(self):
        noise = ['!', '.', ',', '(', ')']
        noise_text_1 = '(dark)ambient'
        clear_text_1 = ' dark ambient'
        self.assertEqual(clear_noise_to(
            noise, noise_text_1, ' '), clear_text_1)

    def test_binary_search(self):
        list = sorted(['cat', 'dog', 'duck', 'bear', 'cow'])
        self.assertEqual(binary_search('cat', list), 1)

    def test_find_all_matches(self):
        core = ['music', 'dog', 'bully']
        text = sorted(['music', 'carry', 'music', 'vorbis', 'dog', 'bully'])
        self.assertEqual(find_all_matches(core, text), 4)


if __name__ == '__main__':
    unittest.main()
