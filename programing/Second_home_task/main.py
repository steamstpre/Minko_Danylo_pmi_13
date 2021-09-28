import numpy as np


def input_num():
    try:
        num = int(input('Your num:'))
    except:
        print('please try num')
        return input_num()
    return num

def input_matrix(n , m):

    matrix = np.zeros((n , m))

    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(m):
            matrix[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    return matrix

def detect_element(matrix , n , m):
    sum_of_elem = 0
    count_of_search_elem = 0
    for i in range(n):
        for j in range(m):
            k =  i
            for k in range(n):
                if(k+1 < n):
                    sum_of_elem =+ matrix[k+1][j]
                else:
                    sum_of_elem =+ matrix[k][j]
                # print(sum_of_elem)
            if(matrix[i][j] > sum_of_elem):
                count_of_search_elem += 1
    #print(count_of_search_elem)
    return count_of_search_elem
def print_hello():
    print("Hello , input type of applying 1 apapply_matrix ,  2 exit ")
    res = input_num()
    return res


def menu():
    res = print_hello()
    while True:
        if res == 2:
            print("exit")
            break
        if res == 1:
            n = input_num()
            if(n < 0):
                n = input_num()
            m = input_num()
            if (m < 0):
                m = input_num()
            our_matrix = input_matrix(n, m)
            our_res = detect_element(our_matrix, n, m)
            print("count of search elements:")
            print(our_res)
            res = print_hello()
        else:
            print("please try num 1 2")
            res = print_hello()

menu()

# n = input_num()
# m = input_num()
# our_matrix =  input_matrix(n , m)
# our_res = detect_element(our_matrix , n , m)
# print("count of search elements:")
# print(our_res)
# for i in range(n):
#     for j in range(m):
#         print(our_matrix[i][j])
