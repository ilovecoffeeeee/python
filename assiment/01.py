def is_on_list(list, day):
    if day in list:
        return True
    else:
        return False


def get_x(list, index):
    return days[index]


def add_x(list, day):
    list.append(day)
    return list


def remove_x(list, day):
    list.remove(day)
    return list


# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
