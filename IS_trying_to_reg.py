def is_trying(id):
    id=str(id)
    file = open("Trying to reg.txt").readlines()
    Flag = False
    for i in range(len(file)):
        if file[i].rsplit('\n')[0] == id:
            Flag = True
    return Flag
