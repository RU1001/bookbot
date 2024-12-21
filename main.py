from collections import Counter
def countCharacters(text):
    text_lower = text.lower()
    char_counter = Counter(text_lower)
    return char_counter

def countWords(text):
    split_book = text.split()
    for word in split_book:
        return(len(split_book))

def sort_on(item):
    return item[1] 

def aggregateReport(text):
    chars = [ch for ch in text if ch.isalpha()]
    char_count = Counter(chars)
    sorted_count = sorted(char_count.items(), key=sort_on, reverse=True)

    for letter, num in sorted_count:
        print(f"the '{letter}' character was found {num} times")
   
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    print(countCharacters(file_contents))
    print(aggregateReport(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countWords(file_contents)} words found in this document")
    aggregateReport(file_contents)
    print("--- End report ---")


if __name__ == "__main__":
    main()
