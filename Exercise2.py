some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_letters = []

for i in some_list:
    if some_list.count(i) > 1:
        if duplicate_letters.count(i) < 1:
            duplicate_letters += i
print(f'Duplicate values in some_list are: {duplicate_letters}')

print(set(some_list))