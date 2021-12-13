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


mem_fish = []


def read_mem(fish, day):
    if ((fish, day) in mem_fish):
        return mem_fish[mem_fish.index((fish, day)) + 1]
    else:
        return None


def write_mem(fish, day, result):
    mem_fish.append((fish, day))
    mem_fish.append(result)


def fish_count(fish, day, result):
    if (day == 0):
        return result
    elif (read_mem(fish, day) != None):
        return read_mem(fish, day)
    elif (fish == 0):
        temp_result = fish_count(6, day - 1, result + 1) + fish_count(8, day - 1, 0)
        write_mem(fish, day, temp_result)
        return temp_result
    else:
        temp_result = fish_count(fish - 1, day - 1, result)
        write_mem(fish, day, temp_result)
        return temp_result


# def fish_count(fish, day):
#     if (day == 0):
#         return 0
#     elif (read_mem(fish, day) != None):
#         return read_mem(fish, day)
#     elif (fish == 0):
#         temp_result = 1 + fish_count(6, day - 1) + fish_count(8, day - 1)
#         write_mem(fish, day, temp_result)
#         return temp_result
#     else:
#         temp_result = fish_count(fish - 1, day - 1)
#         write_mem(fish, day, temp_result)
#         return temp_result


def gen_fish_model(lst, days):
    count = len(lst)
    for fish in lst:
        count += fish_count(fish, days)
    return count

print(gen_fish_model(txt_to_list(), 256))
# print(mem_fish)


