import numpy as np
import random as rand

def input_number():
    try:
        our_num = int(input("enter num: "))
    except:
        print("try number")
        return input_number()
    return our_num

def apply_arr_by_key(n):
    arr = []

    print('Enter Augmented:')
    for i in range(n):
        print('a[' + str(i) + ']')
        our_elem = input_number()
        arr.append(our_elem)

    return arr

def merge_two_list(left_side,right_side , count_of_operation , arr_of_operation):
    res = []
    i = j = 0#pointers
    while(i < len(left_side) and j < len(right_side)):
        if left_side[i] < right_side[j]:
            res.append(left_side[i])
            i+=1
            count_of_operation += 1
        else:
            res.append(right_side[j])
            j+=1
            count_of_operation += 1
    if i < len(left_side):
        res += left_side[i:]
        count_of_operation += 1
    if j < len(right_side):
        res += right_side[j:]
        count_of_operation += 1
    arr_of_operation.append(count_of_operation)
    return res

def return_count_of_operation(arr_of_max_operation):
    print(max(arr_of_max_operation))

def merge_sort(list ,arr_of_operation, count_of_operation = 0 ):
    if len(list)==1:
        return list
    middle = int(len(list)/2)
    count_of_operation += 1
    left_side = merge_sort(list[:middle] ,arr_of_operation , count_of_operation)
    right_side = merge_sort(list[middle:] ,arr_of_operation , count_of_operation)
    return merge_two_list(left_side , right_side , count_of_operation,arr_of_operation)


def apply_arr_by_diapazon(n):
    arr = []
    print("enter first diapazon: ")
    diapazon_a = input_number()
    print("enter second diapazon: ")
    diapazon_b = input_number()

    for i in range(n):
        our_element = int(rand.randint(diapazon_a , diapazon_b))
        arr.append(our_element)
    return arr

def display_arr(arr):
    for i in range(len(arr)):
        print(arr[i])


def print_hello():
    print("Hello , input type of applying 1 apapply_matrix_by_diapazon , 2 apply_matrix_by_key , 3 exit ")
    res = input_number()
    return res

def display_res(our_matrix , arr_of_operation):
    print("your arr: ")
    display_arr(our_matrix)
    sort_arr = merge_sort(our_matrix, arr_of_operation)
    print("sorted arr")
    display_arr(sort_arr)
    print("count of operation:")
    return_count_of_operation(arr_of_operation)

def start_of_program():
    res = print_hello()
    while True:
        arr_of_operation = []
        if res == 3:
            print("exit")
            break
        if res == 1:
            print("size: ")
            n = input_number()
            our_matrix = apply_arr_by_diapazon(n)
            display_res(our_matrix , arr_of_operation)
            res = print_hello()
            arr_of_operation = []
        if res == 2:
            print("size: ")
            n = input_number()
            our_matrix = apply_arr_by_key(n)
            display_res(our_matrix , arr_of_operation)
            res = print_hello()
            arr_of_operation = []
        else:
            print("please try num 1 2 3")

start_of_program()