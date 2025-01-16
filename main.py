def main():
    path = "books/frankenstein.txt"
    text = get_book(path)
    total_count = get_words(text)
    dictionary = count_characters(text)
    print("--- Begin report of Book ---")
    print(f'There are {total_count} words in this document.')
    for letter, count in sorted(dictionary.items()):
        print(f"The '{letter}' character was found {count} times")
    print("--- End Report ---")

def get_book(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents
    
def get_words(text):
    word_count = 0
    words = text.split()
    return (len(words))

def count_characters(text):
    
    lower_case = text.lower()
    alphabet = {}
    for letter in lower_case:
        if letter.isalpha():
            if letter not in alphabet:
                alphabet[letter] = 1
            else:
                alphabet[letter] += 1
    return alphabet
    
    

main()