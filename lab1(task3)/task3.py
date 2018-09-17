def function(list1):
    list2 = []
    for x in list1:
        if isinstance(x, list):
            list2 += function(x)
        else:
            list2.append(x)
    return list2
list1 = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
print(list1)
print (function(list1))
