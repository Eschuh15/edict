dic = {}
with open("dict.txt") as file:
    for line in file:
        (key, val) = line.strip("\n").split("=")
        dic[key] = val

print(dic)
