
def sortFunction(a, b, index = 0):

    if (index == 0):
        return a < b

    return a[index] < b[index]

def selectionSort(list, function, index = 0):

    for x in range(0, len(list) - 1):

        xMin = x
        for y in range(x + 1, len(list)):
            if function(list[y], list[xMin], index):
                xMin = y

        list[xMin], list[x] = list[x], list[xMin]
    return list


def filterList(list, function):
    l = []
    for x in list:
        if function(x):
            l.append(x)

    return l









