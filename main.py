def sort_on(dict):
    return dict["value"]


def read_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_frequency(text):
    frequency_map = {}
    for letter in text:
        add_to_map(frequency_map, letter.lower())
    return frequency_map


def add_to_map(map, letter):
    if map.get(letter) is not None:
        map[letter] += 1
    else:
        map[letter] = 1


def get_sorted_letter_frequency_list(frequency_map):
    list = []
    for key in frequency_map:
        list.append({"letter": key, "value": frequency_map[key]})
    list.sort(reverse=True, key=sort_on)

    return list


def main():
    text = read_text("./books/frankenstein.txt")
    frequency_map = get_char_frequency(text)
    list = get_sorted_letter_frequency_list(frequency_map)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(text)} words found in the document\n")
    for v in list:
        if v["letter"].isalpha():
            print(f"The {v["letter"]} character was found {v["value"]} times")
    print("--- End report ---")


main()
