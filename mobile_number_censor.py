import re
def mobile_number_censor(number):
    numPattern = re.compile(r'^(09|\+639)\d{9}$')
    if numPattern.search(number):
        if number[0] == '+':
            return number[0:4] + '*****' + number[9:13]
        else:
            return number[0:2] + '*****' + number[7:11]
    else:
        return None

mobile_number_censor('09171120338')