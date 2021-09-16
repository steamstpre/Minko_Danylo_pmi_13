def enter_num():#input num
    try:
        count_of_elements = int(input("number: "))
    except:
        print("please enter number:")
        return enter_num()
    return count_of_elements

count_of_elements = enter_num()

def input_our_arr(count_of_elements , our_arr):#input elements
    index = 0
    our_element = 0
    while index < count_of_elements:
        # our_element = int(input('your num: '))
        our_element = enter_num()
        our_arr.append(our_element)
        index += 1



def algoritm(count_of_element , our_arr):
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

    print(our_arr.index(search_element))#print index


our_arr = []
count_of_elements = enter_num()
input_our_arr(count_of_elements , our_arr)
input_our_arr(count_of_elements , our_arr)
algoritm(count_of_elements , our_arr)

