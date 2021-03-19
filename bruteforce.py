def permutations(string):
    if len(string) == 1:
        return set(string)

    recursive_perms = []
    for c in string:
        for perm in permutations(string.replace(c, '', 1)):
            recursive_perms.append(c + perm)

    return set(recursive_perms)

print(permutations('a'))