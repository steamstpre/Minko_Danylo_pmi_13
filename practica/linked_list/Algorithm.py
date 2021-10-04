from Linked_list import LinkedList , Node
import Validation
import random

def algoritm(count_of_element , our_list):
    print("your k: ")
    our_k_dodat = Validation.enter_num()
    our_arr = []
    our_arr = our_list.get_list()
    index = 0
    search_element = 0

    while index < count_of_element:
        if (our_k_dodat > our_arr[index].data and -our_k_dodat < our_arr[index].data):
            search_element = our_arr[index]
            break
        index += 1
    our_arr.reverse()

    print(our_arr.index(search_element))#print index

def input_our_list():#input elements
    print("count of elem:")
    count_of_elements = Validation.enter_num()
    index = 0
    our_arr = LinkedList()
    while index < count_of_elements:
        our_element = Validation.enter_num()
        our_node = Node(our_element)
        our_arr.insert(our_node)
        index += 1
    algoritm(count_of_elements , our_arr)

def generate_our_list():
    our_arr = LinkedList()
    print("diapazon n and m :")
    print("n: ")
    n = Validation.enter_num()
    print("m: ")
    m = Validation.enter_num()
    print("count of elements:")
    count_of_elements = Validation.enter_num()

    for i in range(count_of_elements):
        our_element = random.randint(n , m)
        our_node = Node(our_element)
        our_arr.insert(our_node)
    algoritm(count_of_elements, our_arr)


