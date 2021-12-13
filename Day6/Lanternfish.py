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


def check_timer(lst):
    temp_lst = []

    def helper(x):
        if (x == 0):
            temp_lst.append(9)
            return 7
        else:
            return x
    
    new_lst = list(map(helper, lst))
    new_lst.extend(temp_lst)
    return new_lst


def minus_timer(lst):
    lst = list(map(lambda x: x - 1, lst))
    return lst

def gen_fish_model(lst, day):
    if (day == 0):
        return lst
    else:
        lst = check_timer(lst)
        lst = minus_timer(lst)
        return gen_fish_model(lst, day - 1)

print(len(gen_fish_model(txt_to_list(), 256)))