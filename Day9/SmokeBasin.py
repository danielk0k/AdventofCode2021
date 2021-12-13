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
    temp = []

    for elt in lst:
        split_str = re.findall(regex, elt)
        temp.append(split_str)
    
    return temp


def getLowPoints(matrix):
    len_row = len(matrix)
    len_col = len(matrix[0])
    coord_low_pt = []
    counter = 0

    def helper(row, col):
        if (row < 0 or row == len_row):
            return 10
        elif (col < 0 or col == len_col):
            return 10
        else:
            return int(matrix[row][col])

    for i in range(len_row):
        for j in range(len_col):
            entry = int(matrix[i][j])
            if (entry < helper(i - 1, j) and
                entry < helper(i + 1,j) and
                entry < helper(i, j - 1) and
                entry < helper(i, j + 1)):
                counter += entry + 1
                coord_low_pt.append((i, j))

    return counter, coord_low_pt


mem = []


def read_mem(row, col):
    if ((row, col) in mem):
        return True
    else:
        return False


def write_mem(row, col):
    mem.append((row, col))


def sumBasin(row, col, matrix):
    if (row < 0 or row == len(matrix) or col < 0 or col == len(matrix[0])):
        return 0
    elif (int(matrix[row][col]) == 9 or read_mem(row, col)):
        return 0
    else:
        write_mem(row, col)
        temp_result = 1 + sumBasin(row - 1, col, matrix) + sumBasin(row + 1, col, matrix) + sumBasin(row, col - 1, matrix) + sumBasin(row, col + 1, matrix)
        return temp_result

def main():
    matrix = genMatrix(txt_to_list())
    risk_lvl, low_points = getLowPoints(matrix)
    print("Sum of the risk levels of all low points:", risk_lvl)

    basin_result = []

    for coord in low_points:
        basin_result.append(sumBasin(coord[0], coord[1], matrix))

    basin_result.sort()
    largest_result = basin_result[-1] * basin_result[-2] * basin_result[-3]
    print("Mulitplication of the sizes of the three largest basins:", largest_result)
    
    return "Completed"

print(main())

