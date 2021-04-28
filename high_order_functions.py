from functools import reduce

my_list = [1, 4, 5, 6, 9, 13, 19, 21]

#filter
odd = list(filter(lambda x: x % 2 != 0, my_list))

squares = list(map(lambda x : x**2, my_list))

all_multiplied = list(reduce(a, b : a * b, my_list))
pass