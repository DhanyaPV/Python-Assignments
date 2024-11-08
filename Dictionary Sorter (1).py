def sort_dict_by_keys():
    
    user_input = input("Enter a dictionary (in the format {key1: value1, key2: value2, ...}): ")
    
    try:
        user_dict = eval(user_input)
        if not isinstance(user_dict, dict):
            raise ValueError("The input is not a valid dictionary.")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    sorted_dict = dict(sorted(user_dict.items()))
    
    print("Sorted dictionary by keys:", sorted_dict)
    
sort_dict_by_keys()
