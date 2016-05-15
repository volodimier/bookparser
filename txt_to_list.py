

specials = (',', '.', '!', '?', '"', "'", ':', ';', '(', ')', '*', '-')


def txt_to_list(file):
    """Iterate through the words of .txt file and add them to the list.

    Arg:
        A name of UTF-8 text document.

    Return:
        A list of string containing the unique words from
        the text file.
    """

    unique_words = list()
    for line in file:                # TODO fix this
        words = line.split()
        for word in words:          # TODO rewrite using regexp
            if word in specials:
                continue
            for i in range(5):
                try:
                    if word[-1] in specials:
                        word = word[:-1]
                except IndexError:
                    continue
            for i in range(3):
                try:
                    if word[0] in specials:
                        word = word[1:]
                except:
                    continue
            word = word.lower()
            unique_words.append(word)
    file.close()
    return unique_words
