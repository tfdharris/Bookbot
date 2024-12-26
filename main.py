def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def letter_frequency(text):
    lowered_text = text.lower()
    frequency_dict = {}

    for char in lowered_text:
        if char.isalnum():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

    return frequency_dict

def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        count = word_count(file_contents)
        letters = letter_frequency(file_contents)
        print(count, letters)

main()
