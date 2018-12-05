from itertools import cycle, accumulate
import operator


def getInputs(input='input.txt'):
    with open(input, 'r') as file:
        ops = [int(x) for x in list(file)]
        file.close

    return ops


def calculateFrequency():
    return sum(getInputs())


def getFirstRepeatedFreq():

    # {0}  # set -> O(1) lookup. list -> O(n)
    frequencies = set()
    prevFreq = 0
    currFreq = None
    inputs = getInputs()

    for input in cycle(inputs):
        currFreq = input + prevFreq
        if currFreq in frequencies:
            return currFreq
        else:
            frequencies.add(currFreq)
            prevFreq = currFreq


print(getFirstRepeatedFreq())
