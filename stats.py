def get_book_text(path):
    with open(path) as f:
        file_text = f.read()
    return file_text
def count_words(text):
    return len(text.split())
def count_characters(text):
    dict = {}
    for c in (text):
        if(not c.isalpha()):
            continue
        if(c.lower() in dict):
            dict[c.lower()]+=1
        else:
            dict[c.lower()] = 1
    return dict
def sort_on(items):
    return items["num"]
def sort_dict(dict):
    tmp = []
    for c in dict:
        cnt = dict[c]
        tmp.append({"char":c,"num":cnt})
    tmp.sort(reverse=True,key=sort_on)
    return tmp
