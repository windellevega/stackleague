import hashlib
def crack(hash):
    x = 0
    for x in range(100000):
        string = str(x)
        if len(string) < 5:
            string = '0' * (5 - len(string)) + string
        if hash == hashlib.md5(string.encode()).hexdigest():
            return string


print(crack("827ccb0eea8a706c4c34a16891f84e7b"))
print(crack("86aa400b65433b608a9db30070ec60cd"))