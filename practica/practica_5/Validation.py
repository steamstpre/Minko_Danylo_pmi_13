def enter_num():#input num
    try:
        count_of_elements = int(input("number: "))
    except:
        print("please enter number:")
        return enter_num()
    return count_of_elements

def check_file():
    try:
        our_file = input("file: ")
        open(our_file)
    except:
        print("not correct file")


