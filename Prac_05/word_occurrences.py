def main():
    text = input("Text: ")
    words = text.split()
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    sorted_words_list = list(word_to_count.keys())
    sorted_words_list.sort()
    width = max(len(word) for word in word_to_count.keys())
    for word in sorted_words_list:
        print(f"{word:{width}} : {word_to_count[word]}")


main()
