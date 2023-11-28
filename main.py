def number_of_words(string):
    words = string.split()
    return len(words)

def number_of_letters(string):
    words = string.split()
    dict = {}

    for word in words:
        for i in range(0, len(word)):
            if word[i].lower() not in dict:
                dict[word[i].lower()] = 1
            else:
                dict[word[i].lower()] += 1
    return dict

def get_string_from_location(location):
    with open(location) as f:
        file_contents = f.read()
        return file_contents
    
def dict_to_list(dict):
    new_list = []
    for letter in dict:
        if letter.isalpha():
            new_list.append((letter, dict[letter]))
    new_list.sort(key=lambda a: a[1], reverse=True)
    return new_list
    
def main():
    location = "books/frankstein.txt"
    string = get_string_from_location(location)
    print(f"--- Begin report of {location} ---")
    print(f"{number_of_words(string)} words in the document\n")

    dict = number_of_letters(string)
    new_list = dict_to_list(dict)

    for tuple in new_list:
        print(f'The \'{tuple[0]}\' character was found {tuple[1]} times')
    print("--- End Report ---")

main()