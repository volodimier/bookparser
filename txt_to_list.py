import re


def txt_to_list(file):
    """Iterate through the words of .txt file and add them to the list.

    Arg:
        TextIOWrapper

    Return:
        A list of string containing the unique words from
        the text file.
    """

    unique_words = list()
    for line in file:
        line = re.sub(r'[^\w\s]', '', line)
        words = line.split()
        for word in words:
            word = word.lower()
            unique_words.append(word)
    file.close()
    return unique_words