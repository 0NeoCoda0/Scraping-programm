# Scraping-programm

The program connects to the site gamedev.ru . It uses the semantic core in order to find a word match among the data from the web page. The semantic core is a list of words that indicate the necessary information, in other words, a "white sheet". A "black sheet" is also used, which is presented as a file with water words. These words are irrelevant and should be ignored before analyzing the data of the web page and the "white sheet". The program has no settings for the user and is tailored to one specific task: to find all sound designers on the site gamedev.ru . To adapt the program to the search for other data, it is necessary to create new "black and white sheets", as well as rewrite the scraping algorithm for a specific site.


To see the program in action, you need to run the "parsing" file. The received data will be saved in the "parse_data" folder. The numbers in the name indicate the "id" of the forum page. They need to be inserted into the url link to be on the desired page.

Also, the "test" file contains a few unit tests of the functions used.
