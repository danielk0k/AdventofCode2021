import re

def get_direction(strr):
    regex = r"^(.*)\s(\d*)\n$"
    result = re.search(regex, strr)
    return result.groups()

def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)

# down +X to depth
# up -X to depth
# foward +X depth

def get_position(lst):
    horizontal = 0
    depth = 0
    for elt in lst:
        result_dir = get_direction(elt)
        direction = result_dir[0]
        dist = int(result_dir[1])
        if direction == "forward":
            horizontal += dist
        elif direction == "down":
            depth += dist
        elif direction == "up":
            depth -= dist
        else:
            pass
    return horizontal * depth

print(get_position(txt_to_list()))

def get_position_2(lst):
    horizontal = 0
    depth = 0
    aim = 0
    for elt in lst:
        result_dir = get_direction(elt)
        direction = result_dir[0]
        dist = int(result_dir[1])
        if direction == "forward":
            horizontal += dist
            depth += aim * dist
        elif direction == "down":
            aim += dist
        elif direction == "up":
            aim -= dist
        else:
            pass
    return horizontal * depth

print(get_position_2(txt_to_list()))


