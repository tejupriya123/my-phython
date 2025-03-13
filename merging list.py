def merge_and_remove_duplicates(list1, list2):
    
    merged_list = list(set(list1 + list2))
    return merged_list



list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = merge_and_remove_duplicates(list1, list2)
print("Merged list without duplicates:", result)

def merge_and_remove_duplicates_ordered(list1, list2):
    merged_list = []
    for item in list1 + list2:
        if item not in merged_list:
            merged_list.append(item)
    return merged_list


result_ordered = merge_and_remove_duplicates_ordered(list1, list2)
print("Merged list without duplicates (preserve order):", result_ordered)
