from stack import Stack


s = Stack()

with open('sfile.txt') as fr:
    for lines in fr.readlines():
        s.push(lines.rstrip('\n'))
fr.close()

with open('sfile.txt','w') as fw:
    while not s.is_empty():
        fw.write(s.pop()+'\n')
fw.close()

