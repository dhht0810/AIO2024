def count_chars(s):
    s = s.lower()
    res = {}
    for i in s:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res


string = "Happiness"
print(count_chars(string))
