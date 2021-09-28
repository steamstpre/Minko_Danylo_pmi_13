if __name__ == '__main__':
    from TAX_FREE import Tax_free
    import Operation_with_file
    import Sort
    import Search
    import Menu

# first_company = Tax_free(id_input="123", company_input="aname", vat_rate_input="10", country_input="Italy",
#                              date_of_purchase_input="28.10.2003", vat_code_input="VA-123-12-123",
#                              date_of_tax_ref_input="10.11.1999")
# second_comapany = Tax_free(id_input="0000", company_input="Italy", vat_rate_input="30",
#                                country_input="Germany", date_of_purchase_input="23.11.2003",
#                                vat_code_input="VA-423-12-123", date_of_tax_ref_input="20.03.1999")
# Third_comapany = Tax_free(id_input="0000", company_input="Aecond_name", vat_rate_input="30",
#                               country_input="Germany", date_of_purchase_input="23.03.2003",
#                               vat_code_input="VA-123-12-123", date_of_tax_ref_input="20.11.1999")
#
# arr = [first_company, second_comapany, Third_comapany]
# #
# # #Search.search(arr , "Italy")
# #
# # #Sort.sort(arr)
# # #Sort.sort_by_company(arr)
# # # Sort.sort_by_vac_code(arr)
# Operation_with_file.input(arr , "data_base.bin")
# # # new_arr = Operation_with_file.read("data_base.bin")
# # #new_arr = Operation_with_file.delete_from_data_base("data_base.bin" , "Italy")
# # #
# # Operation_with_file.delete_from_data_base("data_base.bin" , "Italy")
# # new_arr = Operation_with_file.read("data_base.bin")
# # for i in range(len(new_arr)):
# #     print(new_arr[i])

Menu.menu()

