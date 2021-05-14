def party(first, second, maximum):
    merged = []
    for i in range(max(len(first), len(second))):
        if(i < len(first)):
            merged.append(first[i])
        if(i < len(second)):
            merged.append(second[i])

    return merged[0:maximum]

print(party(['Camren'], ['Analy'], 0))
print(party(['Alison'], ['Alison'], 1))
print(party(['Anna', 'Claire', 'Kammy'], ['Lisa', 'Noel', 'Cameron'], 5))