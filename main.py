from stats import word_count
from stats import character_count
from stats import report_char_count
import sys


def get_book_text(path):
  with open(path) as f:
    frankenstein = f.read()
    #print(frankenstein)
    return frankenstein

def pretty_list(dict_list):
  for item in dict_list:
    print(f'{item["char"]}: {item["num"]}')

def main():
  if len(sys.argv) != 2:
    how_to_use = "Usage: python3 main.py <path_to_book>"
    print(how_to_use)
    sys.exit(1)
  else:
    book_location = sys.argv[1]
    frankenstein_text = get_book_text(book_location)
    total_word_count = word_count(frankenstein_text)
    frank_char_count = character_count(frankenstein_text)
    dict_list = report_char_count(frank_char_count)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_location}...')
    print("----------- Word Count ----------")
    print(f'Found {total_word_count} total words')
    print("--------- Character Count -------")
    pretty_list(dict_list)
    print("============= END ===============")
  
main()