our_arr = []
def enter_count_of_elem():
    try:
        count_of_elements = int(input("number: "))
    except:
        print("please enter number:")
        return enter_count_of_elem()
    return count_of_elements

count_of_elements = enter_count_of_elem()

def input_our_arr(count_of_elements , our_arr):
    index = 0
    our_element = 0
    while index < count_of_elements:
        our_element = enter_count_of_elem()
        our_arr.append(our_element)
        index += 1

input_our_arr(count_of_elements , our_arr)

our_k_dodat = int(input("our k: "))
our_arr.reverse()
index = 0
search_element = 0

while index < count_of_elements:
    if(our_k_dodat > our_arr[index] and -our_k_dodat < our_arr[index]):
        search_element = our_arr[index]
        break
    index += 1
our_arr.reverse()

print(our_arr.index(search_element))

#first question
#our arr 2n
# count_of_elements = 1
# our_arr = []
# while (count_of_elements % 2) != 0 :
#     count_of_elements = int(input("Your_count of elements: "))
#
# our_element = 0
# index = 0
#
# #insert in our arr
# while index < count_of_elements:
#     our_element = int(input("your num :"))
#     our_arr.insert(index , our_element)
#     index += 1
#
# #remove elements which > count of elements / 2
# our_element = 0
# new_arr = []
# new_pos = int(count_of_elements / 2)+1
# print(new_pos)
#
# while new_pos < count_of_elements:
#     new_arr.insert(new_pos , our_arr[new_pos])
#     new_pos += 1
#
# new_pos = int(count_of_elements / 2)
# index = 0
# while index < new_pos:
#     new_arr.append(our_arr[index])
#     index += 1
#
# for items in new_arr:
#     print(items)