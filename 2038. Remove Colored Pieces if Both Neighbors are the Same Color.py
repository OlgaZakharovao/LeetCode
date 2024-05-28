colors = list(input())

counter = 1
prev = 'a'

alice = 0
bob = 0

for i in colors:
    if prev == 'a':
        prev = i
    elif i == prev:
        counter += 1
    else:
        if counter > 2:
            if prev == 'A':
                alice += counter - 2
            else:
                bob += counter - 2
        prev = i
        counter = 1
if counter > 2:
    if prev == 'A':
        alice += counter - 2
    else:
        bob += counter - 2
if alice > bob:
    print(True)
else:
    print(False)
