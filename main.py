def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def letter_frequency(text):
    lowered_text = text.lower()
    frequency_dict = {}

    for char in lowered_text:
        if char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

    sort_freq = sorted(frequency_dict.items(), key=lambda x: x[1], reverse = True)
    return sort_freq

def print_report(file_path, text):
    word_count = count_words(text)
    sorted_frequencies = letter_frequency(text)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for char, freq in sorted_frequencies:
        print(f"The '{char}' character was found {freq} times")

    print("--- End Report ---")




def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        sorted_frequencies = letter_frequency(file_contents)
        print_report("books/Frankenstein.txt", file_contents)

main()
