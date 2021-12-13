import itertools


def reduce(function, init, iterable):
    it = iter(iterable)
    if init is None:
        value = next(it)
    else:
        value = init
    for element in it:
        value = function(element, value)
    return value


def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()

        pattern_result = []
        output_result = []

        for line in read_file:
            temp = line.split()
            delimiter_index = temp.index("|")
            pattern_result.append(temp[:delimiter_index])
            output_result.append(temp[delimiter_index + 1:])
        return pattern_result, output_result
    except OSError as Err:
        print(Err)


# def checkPattern(lst):
#     count = 0
#     for pat in lst:
#         len_pat = len(pat)
#         if (len_pat == 2 or len_pat == 3 or len_pat == 4 or len_pat == 7):
#             count += 1
#     return count


seven_seg = [
[1,1,1,0,1,1,1], # zero
[0,0,1,0,0,1,0], # one
[1,0,1,1,1,0,1], # two
[1,0,1,1,0,1,1], # three
[0,1,1,1,0,1,0], # four
[1,1,0,1,0,1,1], # five
[1,1,0,1,1,1,1], # six
[1,0,1,0,0,1,0], # seven
[1,1,1,1,1,1,1], # eight
[1,1,1,1,0,1,1]]  # nine


def getUniquePattern(lst):
    temp = []
    for pat in lst:
        len_pat = len(pat)
        if (len_pat == 2 or len_pat == 3 or len_pat == 4 or len_pat == 7):
            temp.append(pat)
    temp.sort(key=len)
    return temp


def gen_combination(patterns):
    seven_seg_perm = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]))
    copy_seven_seg_perm = seven_seg_perm.copy()

    one_pat = patterns[0]
    seven_pat = patterns[1]
    four_pat = patterns[2]

    for config in seven_seg_perm:
        if (config[2] == one_pat[0] and config[5] == one_pat[1]):
            pass
        elif (config[2] == one_pat[1] and config[5] == one_pat[0]):
            pass
        else:
            try:
                copy_seven_seg_perm.remove(config)
            except:
                pass

    for letter in seven_pat:
        if (letter != one_pat[0] and letter != one_pat[1]):
            for config in seven_seg_perm:
                if (config[0] != letter):
                    try:
                        copy_seven_seg_perm.remove(config)
                    except:
                        pass
    
    four_pat_filtered = list(filter(lambda letter: letter != one_pat[0] and letter != one_pat[1], four_pat))
    for config in seven_seg_perm:
        if (config[1] == four_pat_filtered[0] and config[3] == four_pat_filtered[1]):
            pass
        elif (config[1] == four_pat_filtered[1] and config[3] == four_pat_filtered[0]):
            pass
        else:
            try:
                copy_seven_seg_perm.remove(config)
            except:
                pass

    return copy_seven_seg_perm


def gen_number(output, pattern):
    temp =  [0,0,0,0,0,0,0]

    for letter in output:
        try:
            temp[pattern.index(letter)] = 1
        except:
            pass

    for seven_seg_pattern in seven_seg:
        if (temp == seven_seg_pattern):
            return str(seven_seg.index(seven_seg_pattern))

    return None


def sum_output(lst, pattern):
    if (len(lst) == 0):
        return ""
    else:
        return gen_number(lst[0], pattern) + sum_output(lst[1:], pattern)


# print(gen_number("cdfbe", ["d", "e", "a", "f", "g", "b", "c"]))
# print(gen_combination())

# print(gen_combination(getUniquePattern(txt_to_list()[1])))


def main():
    pattern_result, output_result = txt_to_list()
    length_result = len(pattern_result)
    sum_result = 0

    for i in range(length_result):
        connection = gen_combination(getUniquePattern(pattern_result[i]))
        correct_connection = None

        for combi in connection:
            result = list(map(lambda x: gen_number(x, combi), pattern_result[i]))
            if not(None in result):
                correct_connection = combi
                break

        sum_result += int(sum_output(output_result[i], correct_connection))

    return sum_result


print(main())

# for elt in ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']:
#     print(gen_number(elt, ('d', 'f', 'b', 'e', 'g', 'a', 'c')))

