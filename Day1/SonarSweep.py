def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)

def count_increase(lst):
    count = 0
    prev = 0
    for elt in lst:
        num = int(elt)
        if prev == 0:
            prev = num
        elif num > prev:
            count += 1
            prev = num
        else:
            prev = num
    return count

def count_sum_increase(lst):
    count = 0
    prev = 0
    len_lst = len(lst)
    for i in range(len_lst):
        if i == 3:
            prev = int(lst[i - 1]) + int(lst[i - 2]) + int(lst[i])
        elif i - 1 >= 0 and i - 2 >= 0:
            summ = int(lst[i - 1]) + int(lst[i - 2]) + int(lst[i])
            if summ > prev:
                count += 1
                prev = summ
            else:
                prev = summ
        else:
            pass
    return count

# print(count_increase(txt_to_list()))
# print(count_sum_increase(txt_to_list()))
