#!/usr/bin/env python3

import open_file as fo
import txt_to_list as txt2lst
import list_to_dict as lst2dct
import dict_to_db as dict2db


def execute():
    try:
        file = fo.get_file_name()
        all_words = txt2lst.txt_to_list(file)
        counts = lst2dct.list_to_dict(all_words)
        dict2db.dict_to_db(counts)
        print("The End!")
    except UnboundLocalError:
        print("Sorry, i tried but failed :(")   # TODO !?!?!? исправить этот позор


if __name__ == "__main__":
    execute()
