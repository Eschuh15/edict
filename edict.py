def loader():
dic = {}
with open() as file:
    for line in file:
        (key, val) = line.strip("\n").split("=")
        dic[key] = val
     return dic
