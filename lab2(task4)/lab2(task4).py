import xml.etree.ElementTree as ET

with open('a.txt') as file:
    lines = file.read().split()
    array = [line.replace(",","").replace(".","").split() for line in lines]
dictionary ={}
line = 0
pos = 0
for i in array:
    line += 1
    for j in i:
       pos += 1
       if(j[-3:] not in dictionary):
           dictionary[j[-3:]] = []
       dictionary[j[-3:]].append("("+j + "  line:" + str(line) + " position:" + str(pos)+")")
root = ET.Element("data")
child = ET.SubElement(root, "words")
count=0
for key in dictionary:
    ar = []
    for i in dictionary[key]:
        ar = "; ".join(dictionary[key])
    ET.SubElement(child,"words",word = key,number_of_words=str(len(dictionary[key]))).text = str(ar)
tree = ET.ElementTree(root)
tree.write("list1.xml",encoding='utf-8')