def highest_even(list):
    list.sort()
    list.reverse()
    for item in list:
        if not list[item] % 2:
            return list[item]

print(highest_even([2, 10, 2, 3, 4, 8]))