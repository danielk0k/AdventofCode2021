import math


def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def invertChar(char):
    if (char == ")"):
        return "("
    elif (char == "]"):
        return "["
    elif (char == "}"):
        return "{"
    elif (char == ">"):
        return "<"
    else:
        return ""


def matchChar(entry):
    open_char = ["(", "[", "{", "<"]
    close_char = [")", "]", "}", ">"]
    track_brackets = []

    for char in entry:
        if (char in open_char):
            temp = [char]
            temp.extend(track_brackets)
            track_brackets = temp
        elif (char in close_char):
            if (invertChar(char) == track_brackets[0]):
                track_brackets.pop(0)
            else:
                return char
        else:
            pass
    
    return track_brackets


def sumScore_v1(lst):
    score = 0
    for char in lst:
        if (char == ")"):
            score += 3
        elif (char == "]"):
            score += 57
        elif (char == "}"):
            score += 1197
        elif (char == ">"):
            score += 25137
        else:
            pass
    return score


def sumScore_v2(lst):
    score_lst = []
    for entry in lst:
        temp_sum = 0
        for char in entry:
            if (char == "("):
                temp_sum = temp_sum * 5 + 1
            elif (char == "["):
                temp_sum = temp_sum * 5 + 2
            elif (char == "{"):
                temp_sum = temp_sum * 5 + 3
            elif (char == "<"):
                temp_sum = temp_sum * 5 + 4
        score_lst.append(temp_sum)

    score_lst.sort()
    middle = math.floor(len(score_lst) / 2)
    return score_lst[middle]


def main():
    lst_entry = txt_to_list()
    illegal_result = []
    incomplete_result = []

    for entry in lst_entry:
        temp = matchChar(entry)
        if (type(temp) == str):
            illegal_result.append(temp)
        else:
            incomplete_result.append(temp)
    
    print("score v1:", sumScore_v1(illegal_result))
    print("score v2:", sumScore_v2(incomplete_result))


if __name__ == '__main__':
    main()

