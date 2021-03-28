def remove_duplicated_words(string):
    str_arr = string.split(' ')
    ulist = []
    [ulist.append(x) for x in str_arr if x not in ulist]
    return ' '.join(ulist)

print(remove_duplicated_words("never never ever ever give up on on on your dreams"))
print(remove_duplicated_words("Take Take Take it it it it easy"))