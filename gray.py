on = '█'
off = ' '
length = int(input('Input gray code length: '))
bitList = [' ', '█']

def getNewList(oldList):
    list = oldList.copy()
    for i in range(len(oldList)):
        list.append(oldList[len(oldList) - i - 1])
    for i in range(len(list) // 2):
        list[i] = ' ' + list[i]
        list[len(list) - i - 1] = '█' + list[len(list) - i - 1]
    return list

for i in range(length):
    bitList = getNewList(bitList)
    print('Doubling: ' + str(i + 1) + '/' + str(length + 1))
print('Finished! ' + str(length + 1) + '/' + str(length + 1))
with open("gray_" + str(length) + ".txt", "w") as f:
    for i in range(len(bitList)):
        f.write(bitList[i] + "\n")
