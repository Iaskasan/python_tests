# # X = 'Hadrien'
# # Y = 'Music'

# # print(f'Hello, my name is {X}\nand my hobby is {Y}')

# my_list = [1, 'yolo', True, 5]
# # if len(my_list) == 4:
# # 	if my_list[1] == 'yolo':
# # 		print(my_list)
# print(f'the index of the word {my_list[3]} is {my_list.index(5)}')
# def print_list(list_to_print, n):
# 	print(list_to_print[::(n)])

# exercise_list = [2, 5, 9, 65, 84, 7, 3]
# print_list(exercise_list, 1)

# my_list = exercise_list[0::1]
# print(my_list)

# exercice_list = (1,2,3,4,5,6,7,8,9,10)
# a, b = exercice_list(2, 5)
# print(a, b)

# value_1 = 10
# value_2 = 'test'

# value_1, value_2 = value_2, value_1
# print(f'value_1 is {value_1} and value_2 is {value_2}')

# test_index = 'test'.index('e')
# print(test_index)

# test_string = 'this is a test to test things'
# test_list = [1,2,3,4]

# # print(test_string[2])
# # print(test_string.split())
# # split_string = test_string.split()
# # print(split_string[0])

# # print(" ".join([split_string[1], split_string[4], split_string[5]]))

# # print(tuple(test_list)) # change a list into tuple
# # print(list(test_list)) # change tuple into a list (no way)
# str_int_list = str(test_list) # change int into str
# print(" ".join([str_int_list[1], str_int_list[4], str_int_list[7], str_int_list[10]])) # methode 1
# print(str_int_list.strip('[]').replace(',', '')) #methode 2

###### Dictionnaries ######

# test_dict = {'A' : 123, 'B' : [1,2,3], 1 : True} # {key:value} >> key and value can be of any type
# print(len(test_dict)) # Prints 3 (the number of keys)
# print(list(test_dict)) # Prints a list of the keys / .values() to print the list of values
# print(test_dict['B']) # or print(test_dict.get('B')) > better method
# test_dict.update({'name' : 'Hadrien'})
# # or
# test_dict.update(Age = 34, male = True)
# # or
# test_dict['new_key'] = 100
# print(test_dict)

###### Sets ######
# A list that cannot have duplicated values
# Dups will be removed
# Indexing and slicing does not work

my_set = {1,2,3,4,4}
# print(my_set)

# my_set.add(5)
# my_set.remove(2)
# print(my_set)

new_set = list(my_set)
print(new_set[2]) #exercise

###### comparisons operators ######

set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

print(set1.union(set2)) # adds unique values
print(set1.intersection(set2)) # show values in common
print(set1.difference(set2)) # show the values of set1 that are not present in set2