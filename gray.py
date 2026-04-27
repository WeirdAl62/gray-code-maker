on = '█'
off = ' '
length = int(input('Input gray code length: '))
singleBitList = [' ', '█']

def getNewList(oldList):
    list = oldList.copy()
    for i in range(len(oldList)):
        list.append(oldList[len(oldList) - i - 1])
    for i in range(len(list) // 2):
        list[i] = ' ' + list[i]
        list[len(list) - i - 1] = '█' + list[len(list) - i - 1]
    return list

newList = getNewList(singleBitList)
for i in range(length - 1):
    newList = getNewList(newList)
with open("gray_" + str(length) + ".txt", "w") as f:
    for i in range(len(newList)):
        f.write(newList[i] + "\n")
