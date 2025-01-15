def main():
    path = "books/frankenstein.txt"
    text = get_book(path)
    total_count = get_words(text)
    print(f'There are {total_count} words in this document.')

def get_book(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents
    
def get_words(text):
    word_count = 0
    words = text.split()
    return (len(words))

    
    

main()