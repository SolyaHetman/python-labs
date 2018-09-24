with open('a.txt') as f:
    line = f.readlines()
f.close()

i = 0
with open('a.txt','r') as f:
    with open( 'b1.txt','w') as f1:
            for lines in line:
                i += 1
                if i%2 == 0:
                    lines=lines.upper()
                    f1.write(lines)
f.close()
f1.close()

i = 0
with open('a.txt','r') as f:
    with open( 'b2.txt','w') as f2:
            for lines in line:
                i += 1
                if (i-1)%2 == 0:
                    lines=lines.lower()
                    f2.write(lines)
f.close()
f2.close()

print('File b1')
f1= open('b1.txt','r')
print(f1.read())

print('File b2')
f2= open('b2.txt','r')
print(f2.read())



