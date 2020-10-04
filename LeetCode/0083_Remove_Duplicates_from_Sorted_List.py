def remove_duplicates(lst):
    blank_lst = []
    for i in lst:
        if i not in blank_lst: blank_lst.append(i)
    return blank_lst


print(remove_duplicates([1,2,2,3]))