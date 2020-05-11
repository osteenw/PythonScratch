# from functools import reduce
#
#
# def multiply_by2(item):
#     return item*2
#
# def only_odd(item):
#     return item % 2
#
# my_list = [1, 2, 3]
# your_list = [10, 20, 30]
#
# # print(list(map(multiply_by2, my_list)))
# # print(my_list)
# #
# # print(list(filter(only_odd, my_list)))
# #
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
# #
# # print(reduce(accumulator, my_list, 0))
# # print(my_list)
#
# print(list(map(lambda item: item*2, my_list)))
# my_list = [5,4,3]
#
#
# print(list(map(lambda item: item*item, my_list)))
#
# a = [(0,2), (4,3), (9,9), (10,-1)]
# a.sort(key=lambda x: x[1])
# a.reverse()
# print(a)

# my_list = [char for char in 'hello']
# # for char in 'hello':
# #     my_list.append(char)
# my_list2 = [int for int in range(0, 100)]
# my_list3 = [num for num in range(0, 200, 2)]
# my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
# print(my_list)
# print(my_list4)

# simple_dict = {
#     'a': 1,
#     'b': 2
# }
# my_dict = {key: value ** 2 for key, value in simple_dict.items()}
# my_dict2 = {num:num*2 for num in [1,2,3]}
#
# print(my_dict2)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
# print(duplicates)

# from time import time
#
# def performance(fn):
#     def wrap_func(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         time_difference = t2-t1
#         print(f'Took {time_difference} s')
#         return result
#     return wrap_func
#
# @performance
# def long_time():
#     for i in range(10000):
#         i*5
#
# # long_time()
#
# user1 = {
#     'name': 'Sorna',
#     'valid': True
# }
#
# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     if args[0]['valid']:
#         return fn(*args, **kwargs)
#     else:
#         print('Authentication failed.')
#   return wrapper
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)

while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except:
        print('please enter a number')
    else:
        print('Thank you!')
        break
