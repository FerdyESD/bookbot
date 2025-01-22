def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(source_text):
    return len(source_text.split())

def count_character(string):
    characters = {}
    split_string = list(string)
    for letter in split_string:
        if letter.lower() in characters:
            characters[letter.lower()] += 1
        else:
            characters[letter.lower()] = 1
    return characters

def filter_dictionary(dictionary):
    filtered_dict = {k: v for k, v in dictionary.items() if k.isalpha()}

    sorted_dict = dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict

def main():
    file_contents = read_file("books/frankenstein.txt")

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document\n\n")

    filtered_letters = filter_dictionary(count_character(file_contents))

    for letter in filtered_letters:
        print(f"The '{letter}' character was found {filtered_letters[letter]} times")
    
    print("--- End report ---")

main()