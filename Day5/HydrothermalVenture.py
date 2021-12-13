# def reduce(function, init, iterable):
#     it = iter(iterable)
#     if init is None:
#         value = next(it)
#     else:
#         value = init
#     for element in it:
#         value = function(element, value)
#     return value


def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def get_coordinate(strr):
    input_strr = strr.split()
    start_pt = input_strr[0].split(",")
    end_pt = input_strr[2].split(",")
    return start_pt, end_pt


def coordinate_gen(start_pt, end_pt):
    start_x = int(start_pt[0])
    start_y = int(start_pt[1])
    end_x = int(end_pt[0])
    end_y = int(end_pt[1])

    if (start_x == end_x):
        result = []
        if (start_y < end_y):
            for y in range(start_y, end_y + 1):
                result.append((start_x, y))
            return result
        else:
            for y in range(end_y, start_y + 1):
                result.append((start_x, y))
            return result
    elif (start_y == end_y):
        result = []
        if (start_x < end_x):
            for x in range(start_x, end_x + 1):
                result.append((x, start_y))
            return result
        else:
            for x in range(end_x, start_x + 1):
                result.append((x, start_y))
            return result
    elif abs((end_y - start_y) / (end_x - start_x)) == 1:
        result = []
        if (start_x < end_x):
            if (start_y < end_y):
                x_coord = start_x
                y_coord = start_y
                while x_coord != end_x and y_coord != end_y:
                    result.append((x_coord, y_coord))
                    x_coord += 1
                    y_coord += 1
                result.append((end_x, end_y))
                return result
            elif (start_y > end_y):
                x_coord = start_x
                y_coord = start_y
                while x_coord != end_x and y_coord != end_y:
                    result.append((x_coord, y_coord))
                    x_coord += 1
                    y_coord -= 1
                result.append((end_x, end_y))
                return result
        elif (start_x > end_x):
            if (start_y > end_y):
                x_coord = start_x
                y_coord = start_y
                while x_coord != end_x and y_coord != end_y:
                    result.append((x_coord, y_coord))
                    x_coord -= 1
                    y_coord -= 1
                result.append((end_x, end_y))
                return result
            elif (start_y < end_y):
                x_coord = start_x
                y_coord = start_y
                while x_coord != end_x and y_coord != end_y:
                    result.append((x_coord, y_coord))
                    x_coord -= 1
                    y_coord += 1
                result.append((end_x, end_y))
                return result
    else:
        return []


def get_lst_all_coordinates(lst):
    coord_lst = []

    for elt in lst:
        start_pt, end_pt = get_coordinate(elt)
        coord_lst.extend(coordinate_gen(start_pt, end_pt))

    return coord_lst


# def remove_all(lst, x):
#     if (x in lst):
#         lst.remove(x)
#         return remove_all(lst, x)
#     else:
#         return lst


# def count_duplicates(lst):
#     def helper(lst, counter):
#         if (len(lst) == 0):
#             return counter
#         else:
#             elt = lst[0]
#             if (lst.count(elt) > 1):
#                 removed_lst = remove_all(lst, elt)
#                 return helper(removed_lst, counter + 1)
#             else:
#                 removed_lst = remove_all(lst, elt)
#                 return helper(removed_lst, counter)

#     return helper(lst, 0)


def count_duplicates(lst):
    tracking_lst = []
    counter = 0

    for elt in lst:
        if not(elt in tracking_lst):
            if (lst.count(elt) > 1):
                counter += 1
                tracking_lst.append(elt)
            else:
                tracking_lst.append(elt)

    return counter


def main():
    return count_duplicates(get_lst_all_coordinates(txt_to_list()))

print(main())


