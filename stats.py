def word_count(text):
  words = text.split()
  total_word_count = len(words)
  return total_word_count
  
  
def character_count(text):
  char_count = {}
  chars = text.lower()
  for c in chars:
    if c not in char_count:
      char_count[c] = 1
    elif c in char_count:
      char_count[c] += 1
  return char_count

def sort_on(items):
  return items["num"]

def report_char_count(char_dict: dict):
  dict_list = []
  for k, v in char_dict.items():
    if k.isalpha():
      dict_list.append({"char": k, "num": v})
  dict_list.sort(key=sort_on, reverse=True)
  return dict_list

# Example of Over thinking the solution ... smh
# def character_count(text):
#   char_count = {}
#   chars = text.lower()
#   for i in range(0, len(chars)):
#     if chars[i] not in char_count:
#       char_count[chars[i]] = 1
#     elif chars[i] in char_count:
#       char_count[chars[i]] = char_count[chars[i]] + 1
#   print(char_count)