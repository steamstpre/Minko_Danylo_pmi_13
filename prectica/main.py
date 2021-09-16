import itertools
import numpy

#генеруєм всі можливі комбінації до певної довжини к , тобто зі всіх елемнтів числення
#і викикдуєм повторні елементи з тої таблиця істиності

def input_num():
    try:
        num = int(input('Your num:'))
    except:
        print('please try num')
        return input_num()
    return num

def check_n():
    n = 0
    while n <= 2:
        n = input_num()
    return n
def check_k():
    k = 0
    while k <= 2  or k >= 10:
        k = input_num()
    return k


def check_n_and_k(k = 0 , n = 0):
    while n+k <= 4 or n+k >= 10:
        k = check_k()
        n = check_n()

check_n_and_k()


def apply_k(k):#all avaluable value
    index = 0
    our_arr = []
    while index < k:
        our_arr.append(index)
        index += 1
    return our_arr

table = list(itertools.product(apply_k(k), repeat=n))

count_of_our_elements = 0
for items in table:
    print(items)

def search_our_count_of_elem(table):
    count_of_our_elements = 0
    for item in table:
        index = 0
        while index < n:
            if index + 1 < len(item) and item[index] == 0 and item[index + 1] == 0:
                count_of_our_elements += 1
                break
            index += 1
    return count_of_our_elements

our_res =  search_our_count_of_elem(table)

print(our_res)
