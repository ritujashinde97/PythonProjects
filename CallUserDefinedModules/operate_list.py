
import random

def delete_name(person_list , target):
    while True :
        if target in person_list:
            person_list.remove(target)
        else :
            print(target + '  is not in the list')
            break

def add_names(person_list , new_name, times):
    if new_name not in person_list:
        for i in range(times):
            person_list.append(new_name)
        random.shuffle(person_list)