import re

def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def genMatrix(lst):
    regex = r"\d"
    result = []
    for entry in lst:
        temp = re.findall(regex, entry)
        result.append(list(map(lambda x: int(x), temp)))
    return result


def upEnergy(matrix):
    len_row = len(matrix)
    len_col = len(matrix)

    for i in range(len_row):
        for j in range(len_col):
            matrix[i][j] += 1
    
    return matrix


def genSurroundingCoord(max_row, row, max_col, col):
    coord_lst = []
    
    def helper(row, col):
        if not(row < 0 or row  == max_row or col < 0 or col == max_col):
            coord_lst.append((row, col))
    
    helper(row - 1, col)
    helper(row - 1, col - 1)
    helper(row - 1, col + 1)
    helper(row, col - 1)
    helper(row, col + 1)
    helper(row + 1, col)
    helper(row + 1, col - 1)
    helper(row + 1, col + 1)
    return coord_lst


def genLstToAdd(lst):
    temp = []
    for coord in lst:
        if (coord not in temp):
            count_coord = lst.count(coord)
            temp.append(coord)
            temp.append(count_coord)
    return temp


def checkMatrix(matrix):
    for row in matrix:
        for elt in row:
            if (elt > 9):
                return True
    return False


def checkMatrixSync(matrix):
    for row in matrix:
        for elt in row:
            if (elt != 0):
                return True
    return False


def checkFullEnergy(matrix):
    len_row = len(matrix)
    len_col = len(matrix)
    full_energy_lst = []

    while (checkMatrix(matrix)):
        new_full_energy_lst = []
        surr_coord_lst = []
        for i in range(len_row):
            for j in range(len_col):
                if (matrix[i][j] > 9):
                    matrix[i][j] = 0
                    full_energy_lst.append((i, j))
                    new_full_energy_lst.append((i, j))

        for coord in new_full_energy_lst:
            surr_coord_lst.extend(genSurroundingCoord(len_row, coord[0], len_col, coord[1]))

        surr_coord_lst = list(filter(lambda x: x not in full_energy_lst, surr_coord_lst))
        temp_surr_coord_lst = genLstToAdd(surr_coord_lst)
        for k in range(0, len(temp_surr_coord_lst), 2):
            matrix[temp_surr_coord_lst[k][0]][temp_surr_coord_lst[k][1]] += temp_surr_coord_lst[k + 1]
            
    return len(full_energy_lst)


def main1(steps):
    matrix = genMatrix(txt_to_list())
    def stepper(steps, counter):
        if (steps == 0):
            return counter
        else:
            return stepper(steps - 1, counter + checkFullEnergy(upEnergy(matrix)))
    return stepper(steps, 0)

print("Number of flashes:", main1(100))


def main2():
    matrix = genMatrix(txt_to_list())
    steps = 0

    while checkMatrixSync(matrix):
        checkFullEnergy(upEnergy(matrix))
        steps += 1

    return steps

print("All flash at step:", main2())

