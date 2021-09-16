
def input_num():
    try:
        count_of_elements = int(input("number: "))
    except:
        print("please enter number:")
        return input_num()
    return count_of_elements

def input_our_arr(count_of_elements , our_arr):
    index = 0
    our_element = 0
    while index < count_of_elements:
        our_element = input_num()
        our_arr.append(our_element)
        index += 1

def algoritm(count_of_elements ,our_arr):
    our_k_dodat = int(input("our k: "))
    our_arr.reverse()
    index = 0
    search_element = 0

    while index < count_of_elements:
        if (our_k_dodat > our_arr[index] and -our_k_dodat < our_arr[index]):
            search_element = our_arr[index]
            break
        index += 1
    our_arr.reverse()

    print(our_arr.index(search_element))

our_arr = []
count_of_elements = input_num()
input_our_arr(count_of_elements , our_arr)
algoritm(count_of_elements , our_arr)

