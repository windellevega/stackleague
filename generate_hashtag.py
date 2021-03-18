def generate_hashtag(s):
    if s == '':
        return False
    hashtag = '#'
    words = s.split();
    for word in words:
        hashtag += word.capitalize()

    if len(hashtag) > 140:
        return False

    return hashtag

print(generate_hashtag(''))