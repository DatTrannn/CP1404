import wikipedia


def main():
    search_phrase = input("Enter page title: ")
    while search_phrase != '':
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print("Page:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        search_phrase = input("Enter page title: ")
    print("End program!")


if __name__ == '__main__':
    main()
