def count_element_occurrences(lst, element):
    return lst.count(element)



if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 2, 2, 5, 2]
    element_to_count = 2
    
    count = count_element_occurrences(my_list, element_to_count)
    print(f"Element {element_to_count} appears {count} times in the list.")
