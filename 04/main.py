from datetime import datetime

# year-month-day hour:minute

# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up


def get_log(input='input.txt'):
    with open(input, 'r') as file:
        # I don't think the hard slices are an elegant solution
        log = []
        for line in list(file):
            k = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')  # time
            if '#' in line:
                # guard id if there, otherwise, log message
                v = int(line[27:].split(' ')[0])
            else:
                v = line[19:-1]
            log.append((k, v))
        file.close

    return log


def get_sorted_log(log=get_log()):  # sort by date
    return sorted(log, key=lambda entry: entry[0])


def get_guards_sleeptime(log=get_sorted_log()):
    guards = {}
    for entry in log:
        if isinstance(entry[1], int):
            id = entry[1]
            last_guard = id
            if id in guards:
                guards[id].append((entry[0], True))
            else:
                guards[id] = [(entry[0], True)]
        elif entry[1] == 'wakes up':
            guards[last_guard].append((entry[0], True))
        else:
            guards[last_guard].append((entry[0], False))

    return guards

# this is where the 'slice not hashable' issue was happening,
# because I was trying to slice the dict get_log returned (you can't slice dicts).
# try list comprehension in get_log instead of for loop
# print(get_log())

# print(sort_log())


print(get_guards_sleeptime())
