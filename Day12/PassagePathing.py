def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def convertNodes(lst):
    result = []
    for entry in lst:
        temp = entry[:-1].split("-")
        if ("start" not in temp and "end" not in temp):
            result.append(temp)
            result.append([temp[1], temp[0]])
        elif (temp[0] == "end" or temp[1] == "start"):
            result.append([temp[1], temp[0]])
        else:
            result.append(temp)
    return result


def findConnections(node, lst):
    temp = []
    for entry in lst:
        if (entry[0] == node):
            temp.append(entry[1])
    return temp


def genPaths(node, lst, prev):
    if (node == "end"):
        return ["end"]
    elif (node.islower() and node != "start" and node != "end"):
        if (node in prev):
            return []
        else:
            temp = []
            for connection in findConnections(node, lst):
                temp.extend(list(map(lambda x: node + "," + x, genPaths(connection, lst, prev + [node]))))
            return temp
    else:
        temp = []
        for connection in findConnections(node, lst):
            temp.extend(list(map(lambda x: node + "," + x, genPaths(connection, lst, prev + [node]))))
        return temp

# print(len(genPaths("start", convertNodes(txt_to_list()), [])))


def checkDuplicate(lst):
    for elt in lst:
        if (elt.islower() and lst.count(elt) > 1):
            return True
    return False


def genPaths_v2(node, lst, prev):
    if (node == "end"):
        return ["end"]
    elif (node.islower() and node != "start" and node != "end"):
        if (node in prev):
            if (checkDuplicate(prev)):
                return []
            else:
                temp = []
                for connection in findConnections(node, lst):
                    temp.extend(list(map(lambda x: node + "," + x, genPaths_v2(connection, lst, prev + [node]))))
                return temp
        else:
            temp = []
            for connection in findConnections(node, lst):
                temp.extend(list(map(lambda x: node + "," + x, genPaths_v2(connection, lst, prev + [node]))))
            return temp
    else:
        temp = []
        for connection in findConnections(node, lst):
            temp.extend(list(map(lambda x: node + "," + x, genPaths_v2(connection, lst, prev + [node]))))
        return temp

print(len(genPaths_v2("start", convertNodes(txt_to_list()), [])))
