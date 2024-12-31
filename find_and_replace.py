import re
# sliding window approach
def findAndReplace(text,oldText,newText):
    not_search_indexes = {}
    len_of_sliding_window = len(oldText)
    return_string = text
    for i,u in enumerate(text):
        if i < len(text)- len(oldText) + 1 and i not in not_search_indexes:
            if text[i:len_of_sliding_window + i] == oldText:
                for indexes in range(i,i+len(oldText)):
                    not_search_indexes[i] = True
                return_string = return_string[:i] + newText + return_string[i+len(oldText):]
    return return_string

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
    
