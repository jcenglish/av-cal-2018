def getInputs(input='input.txt'):
    with open(input, 'r') as file:
        inputs = [x[:26] for x in list(file)]
        file.close

    return inputs


def getSortedInputs():
    return [''.join(sorted(x[:26])) for x in getInputs()]


def countDuplicates():
    doubles = 0
    triples = 0
    ids = getSortedInputs()

    for id in ids:
        i = 0
        gotDouble = False
        gotTriple = False
        while i < len(id):
            if id.count(id[i]) == 2 and not gotDouble:
                doubles += 1
                i += 2
                gotDouble = True
            elif id.count(id[i]) == 3 and not gotTriple:
                triples += 1
                i += 3
                gotTriple = True
            else:
                i += 1

    return doubles * triples


def getIdsAsASCII():
    ids = getInputs()
    idsAscii = []
    for id in ids:
        idsAscii.append([ord(char) for char in id])

    return idsAscii


def getIdDiff():
    ids = getInputs()

    for id1 in ids:
        for id2 in ids:
            count = 0
            for i, char in enumerate(id2):
                if count > 1:
                    count = 0
                    break
                if id1[i] != id2[i]:
                    count += 1
                if count == 1 and i == len(id1) - 1 and id1[i] == id2[i]:
                    return ''.join([ch for i, ch in enumerate(id1) if ch == id2[i]])


'''
    for id1 in ids:
        for id2 in ids[1:]:
            if len(int(id1) & int(id2)) == (len(id1) - 1):
                return ''.join((char(id1) & id2))

'''
print(getIdDiff())
