def enter_num():#input num
    try:
        count_of_elements = int(input("number: "))
    except:
        print("please enter number:")
        return enter_num()
    return count_of_elements