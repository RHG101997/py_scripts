def ox(s):
    x = ["x" for letter in s if letter == "x"]
    o = ["x" for letter in s if letter == "o"]
    if len(x) == len(o):
        return True
    else:
        return False


print(ox("xo(xxxxAxxxxxoxooxooxoxoxobxxxxxxooooooxxxxxooxo)"))