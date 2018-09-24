import xml.etree.ElementTree as ET

with open('a.txt') as f:
    line = f.read().split()
f.close()

count = {}
with open('a.txt')as f:
        for w in line:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
root = ET.Element("data")
child = ET.SubElement(root, "word")
for word, times in count.items():
    ET.SubElement(child, "words", name=word).text = "count=" + str(times)

tree = ET.ElementTree(root)
tree.write("list.xml",encoding='utf-8')