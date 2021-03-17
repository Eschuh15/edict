def loader(fname):
    dic = {}
    with open(fname) as file:
        for line in file:
            (key, val) = line.strip("\n").split("=")
            dic[key] = val
        return dic
