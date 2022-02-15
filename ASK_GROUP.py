def group(id):
    id=str(id)
    file = open("people.txt", 'r').readlines()
    s = dict()
    for i in range(len(file)):
        a = file[i].split(':')[0]
        b = file[i].split(':')[1].rsplit('\n')[0]
        s[a] = b
    if id in s.keys():
        return s[id]
    else:
        return "NO"
