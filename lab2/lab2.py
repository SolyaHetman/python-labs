with open('test.txt') as f:
    line = f.readlines()
f.close()
n = int(input('Enter line:'))

i = 0
with open('test.txt','w') as f:
    for lines in line:
        i += 1
        if i == n:
            edit = lines + 'Hello '
            f.write(edit)
        else:
            f.write(lines)

f.close()

if  n > i:
    print('There no this line!')
else:
    f = open('test.txt','r')
    print(f.read())

