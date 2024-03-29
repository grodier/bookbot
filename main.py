def main():
  with open("books/frankenstein.txt") as f:
    file_conents = f.read()
    total_words = number_of_words(file_conents)
    char_list = filter_non_alpha(to_char_dict_list(characters_in_string(file_conents)))
    char_list.sort(key=sort_on, reverse=True)
    print_report(char_list, total_words, "books/frankenstein.txt")
    
def number_of_words(string):
  words = string.split()
  return len(words)

def characters_in_string(string):
  lowercase_string = string.lower()
  character_map = {}
  for c in lowercase_string:
    if c in character_map:
      character_map[c] += 1
    else:
      character_map[c] = 1
  return character_map

def to_char_dict_list(dict):
  new_list = []
  for key, value in dict.items():
    new_list.append({"char": key, "count": value})
  return new_list

def filter_non_alpha(list):
  filtered_list = []
  for item in list:
    if item["char"].isalpha():
      filtered_list.append(item)
  return filtered_list

def sort_on(dict):
  return dict["count"]

def print_report(list, total_words, document_name):
  print(f"--- Begin report of {document_name} ---")
  print(f"{total_words} words found in the document")
  print("")
  for item in list:
    print(f"The '{item['char']}' character appears {item['count']} times")
  print("--- End of report ---")

main()