def extract(object, propertyName):
    print(object)
    val = ''
    if type(object) is str or type(object) is int:
        return ''
    if len(object) == 1:
        if propertyName in object.keys():
            return object[propertyName]
        elif object.values() is dict or object.values() is list:
            extract(object.values(), propertyName)
        else:
            return ''

    for obj in object:
        if obj == propertyName:
            return object[propertyName]
        if(type(obj) is str or type(obj) is int):
            val = extract(object[obj], propertyName)
        elif (type(obj) is dict):
            val = extract(obj, propertyName)
    return val

obj = {
      'a': '12'
    }
print(extract(obj, 'a'))

obj = {
      'a': [1, 2, 3, 4, {'c': {'x' : 5}}]
    }
print(extract(obj, 'x'))

obj = {
      'a': '12',
      'b': [1,2,3,4,5, {'c': 23}]
    }
print(extract(obj, 'c'))