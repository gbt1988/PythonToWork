import pprint

messages = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in messages:
    count.setdefault(character,0)
    count[character] = count[character] + 1

#pprint.pprint(count)
print(pprint.pformat(count))
pprint.pformat(count)
