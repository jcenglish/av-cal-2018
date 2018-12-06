import datetime

# year-month-day hour:minute

# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up


def get_log(input='input.txt'):
    with open(input, 'r') as file:
        # I don't think the hard slices are an elegant solution
        log = {}
        for line in list(file):
            k = line[1:17]
            if '#' in line:
                v = line[27:].split(' ')[0]
            else:
                v = line[19:-1]
            log[k] = v
        file.close

    return log


# def sort_log():

# this is where the 'slice not hashable' issue was happening.
# try list comprehension ^^^
print(get_log())
