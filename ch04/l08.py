def sum_nested_list(nested_list):
    total_size = 0

    for item in nested_list:
        if type(item) is int:
            total_size += item
            
        else:
            total_size += sum_nested_list(item)
    
    return total_size
