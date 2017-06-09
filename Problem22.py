def name_value(name):
    value = 0
    for c in name:
        value += ord(c.lower()) - 96  # get positional value of letter, add it to 'value'
    return value


f = open('names.txt', 'r')  # open file for reading
names = [name.strip('\"') for name in f.read().split(',')] # put all names in list and strip quotes from all
names.sort()
total_names_score = 0
for name in names:
    total_names_score += name_value(name) * (names.index(name) + 1)

print(total_names_score)
