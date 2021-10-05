from TAX_FREE import Tax_free

def search(arr , search_elem):
    length = len(arr)
    temp_arr = arr
    res_arr = []
    for i in range(length):
        if (temp_arr[i].id == search_elem or temp_arr[i].date_of_purchase == search_elem or temp_arr[i].company == search_elem or temp_arr[i].country == search_elem or temp_arr[i].date_of_tax_ref == search_elem or temp_arr[i].vat_code == search_elem or temp_arr[i].vat_rate == search_elem) and i < length:
            res_arr.append(temp_arr[i])
    return res_arr


