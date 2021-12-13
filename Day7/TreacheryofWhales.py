def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        read_file = read_file[0].split(",")
        read_file = list(map(lambda x: int(x), read_file))
        return read_file
    except OSError as Err:
        print(Err)


def cal_cost(lst, pos):
    result = 0
    for elt in lst:
        result += abs(pos - elt)
    return result


# print(cal_cost(txt_to_list(), 358))


def partial_sum(end):
    return (end / 2) * (end + 1)

def cal_cost_v2(lst):
    max_num = max(lst)
    min_num = min(lst)
    result = 0
    prev_result = 0

    for pos in range(min_num, max_num + 1):
        for elt in lst:
            result += partial_sum(abs(pos - elt))
        if (result < prev_result):
            prev_result = result
            result = 0
        elif (prev_result == 0):
            prev_result = result
        else:
            result = 0
    return prev_result


print(cal_cost_v2(txt_to_list()))
