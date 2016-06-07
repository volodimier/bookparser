import sys


def get_file_name():
    """Get filename from user.

    Return:
        TextIOWrapper
    """

    # TODO add with as

    try:
        filename = sys.argv[1]
    except IndexError:
        filename = input("Enter file name: ")
        if len(filename) < 1:
            filename = 'ipsum.txt'
    try:
        file = open(filename)
        return file
    except FileNotFoundError as e:
        print("File not found error: {}".format(str(e)), file=sys.stderr)
    except UnicodeDecodeError:
        print("Wrong file format!")

