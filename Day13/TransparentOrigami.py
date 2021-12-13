def accumulate(function, init, iterable):
    value = init
    for element in iter(iterable):
        value = function(element, value)
    return value


def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        split_index = read_file.index("\n")
        return read_file[:split_index], read_file[split_index + 1:]
    except OSError as Err:
        print(Err)


def genMatrix(lst):
    coord_lst_temp = list(map(lambda x: x[:-1].split(","), lst))
    coord_lst = list(map(lambda x: [int(x[0]), int(x[1])], coord_lst_temp))
    
    max_x = accumulate(lambda x, y: x[0] if x[0] > y else y, 0, coord_lst)
    max_y = accumulate(lambda x, y: x[1] if x[1] > y else y, 0, coord_lst)
    
    matrix = []
    # initialise matrix
    for i in range(max_y + 1):
        matrix.append([])
        for j in range(max_x + 1):
            matrix[i].append(".")
    
    for dot in coord_lst:
        matrix[dot[1]][dot[0]] = "#"
    
    return matrix


def genInstr(lst):
    instr_lst = []
    for entry in lst:
        temp = entry.split()[2]
        instr_lst.append([temp[0], int(temp[2:])])
    return instr_lst


def folding(axis, num, matrix):
    len_x = len(matrix[0])
    len_y = len(matrix)
    if (axis == "x"):
        flip_index = 0
        for i in range(num - 1, -1, -1):
            flip_index += 2
            for j in range(len_y):
                if (matrix[j][i] == "#"):
                    matrix[j][i + flip_index] = "#"
        for k in range(0, num + 1):
            for m in range(len_y):
                matrix[m].pop(0)

    elif (axis == "y"):
        flip_index = 0
        for i in range(num + 1, len_y):
            flip_index += 2
            for j in range(len_x):
                if (matrix[i][j] == "#"):
                    matrix[i - flip_index][j] = "#"
        for k in range(num, len_y):
            matrix.pop(-1)


def countDot(matrix):
    len_x = len(matrix[0])
    len_y = len(matrix)
    counter = 0
    for i in range(len_y):
        for j in range(len_x):
            if (matrix[i][j] == "#"):
                counter += 1
    return counter


def main1():
    dot_lst, instr_lst = txt_to_list()
    instr = genInstr(instr_lst)
    matrix = genMatrix(dot_lst)
    
    for entry in instr:
        folding(entry[0], entry[1], matrix)
    
    print("Number of dots:", countDot(matrix))
    return matrix

print(main1())
