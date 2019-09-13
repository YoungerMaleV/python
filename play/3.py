count = 0
while count <= 5:
    print('loop', count)
    if count == 6:
        break
    count += 1
else:
    print('loop is done...')

print('out of loop')