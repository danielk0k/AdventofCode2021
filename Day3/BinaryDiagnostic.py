def txt_to_list():
    try:
        myfile = open("input.txt", "r")
        read_file = myfile.readlines()
        myfile.close()
        return read_file
    except OSError as Err:
        print(Err)


def get_bin_count(lst):
    ones_count = 0
    zeros_count = 0
    gamma_rate = ""
    epsilon_rate = ""
    pos = 0

    while pos < 12:
        for elt in lst:
            bin_num = elt[pos]
            if bin_num == "1":
                ones_count += 1
            elif bin_num == "0":
                zeros_count += 1

        if ones_count >= zeros_count:
            gamma_rate += "1"
            epsilon_rate += "0"

        else:
            gamma_rate += "0"
            epsilon_rate += "1"
        
        ones_count = 0
        zeros_count = 0
        pos += 1
    
    gamma_rate_num = int(gamma_rate, 2)
    epsilon_rate_num = int(epsilon_rate, 2)

    print("Gamma Rate:", gamma_rate_num, "\nEpsilon Rate:", epsilon_rate_num)
    return "Power Consumption: " + str(gamma_rate_num * epsilon_rate_num)


print(get_bin_count(txt_to_list()))


def filter_common(lst, pos, mode):
    if len(lst) == 1:
        return lst

    ones_count = 0
    zeros_count = 0

    for elt in lst:
        bin_num = elt[pos]
        if bin_num == "1":
            ones_count += 1
        elif bin_num == "0":
            zeros_count += 1

    # mode True -> get most common value (oxygen generator rating)
    # mode False -> get least common value (CO2 scrubber rating)

    if mode == True:
        if ones_count > zeros_count:
            return filter(lambda x : x[pos] == "1", lst)
        elif zeros_count > ones_count:
            return filter(lambda x : x[pos] == "0", lst)
        elif zeros_count == ones_count:
            return filter(lambda x : x[pos] == "1", lst)
    elif mode == False:
        if ones_count < zeros_count:
            return filter(lambda x : x[pos] == "1", lst)
        elif zeros_count < ones_count:
            return filter(lambda x : x[pos] == "0", lst)
        elif zeros_count == ones_count:
            return filter(lambda x : x[pos] == "0", lst)


def filter_lst(lst):
    oxygen_gen = list(filter_common(lst, 0, True))
    CO2_scrubber = list(filter_common(lst, 0, False))

    for i in range(1, 12):
        oxygen_gen = list(filter_common(oxygen_gen, i, True))
        CO2_scrubber = list(filter_common(CO2_scrubber, i, False))

    oxygen_gen_rate = int(oxygen_gen[0][:12], 2)
    CO2_scrubber_rate = int(CO2_scrubber[0][:12], 2)

    print("Oxygen Generator Rating:", oxygen_gen_rate, "\nCO2 Scrubber Rating:", CO2_scrubber_rate)
    return "Life Support Rating: " + str(oxygen_gen_rate * CO2_scrubber_rate)

print(filter_lst(txt_to_list()))

