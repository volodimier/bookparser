def list_to_dict(list_of_words):
    """Parsing a list of strings.

    Arg:
        List of strings.

    Return:
        A dictionary of strings as a key and integers as a value.
    """
    cnt = dict()
    for word in list_of_words:
        cnt[word] = cnt.get(word, 0)+1
    return cnt