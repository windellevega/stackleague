def sort_mark(lst):
    lst = sorted(lst)
    first = lst[0]
    first = list(first)
    first = '---'.join(first)
    return first

sort_mark(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])