def dynamic_sorting():

    """ 
    allows the user to input a list of elements and dynamically sorts the list based on the specified sorting order 
    """

    try:
        # lenght of the list
        num_elements = int(input("Enter the number of elements you want to add to the list: "))

        # input from the user for each element
        unsorted_list = []
        for _ in range(num_elements):
            element = int(input("Enter an element: "))
            unsorted_list.append(element)

        
        print("Original List:", unsorted_list)

        # Ask the user for sorting order
        sort_order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")

        
        for i in range(0, len(unsorted_list)):
            for j in range(i + 1, len(unsorted_list)):
                # Check sorting order based on user input
                if (sort_order == 'asc' and unsorted_list[i] >= unsorted_list[j]) or (sort_order == 'desc' and unsorted_list[i] <= unsorted_list[j]):
                    unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

        return unsorted_list

    except ValueError:
        print("ERROR! Please enter a valid integer for the number of elements.")


result=dynamic_sorting()
print(result)