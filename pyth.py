def get_middle(s):
    if len(s) % 2 == 0:
        c = int(len(s) / 2)
        return s[c-1:c+1]
    else:
        c = int(len(s) / 2)
        return s[c]