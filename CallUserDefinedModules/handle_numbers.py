

def add_number(num_list , start, num_elements_from_start) :
    return(sum(num_list[start : start + num_elements_from_start]))

def get_mean(num_list ,start, num_elements_from_start) :
    temp_list = num_list[start : start + num_elements_from_start]
    total = 0
    for i in temp_list:
        total += i
    return total / len(temp_list)
