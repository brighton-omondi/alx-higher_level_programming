def common_elements(set_1, set_2):
    # Initialize an empty set to store the common elements
    common_set = set()

    # Iterate through the elements of set_1
    for element in set_1:
        # If the element is present in set_2, add it to the common_set
        if element in set_2:
            common_set.add(element)

    return common_set