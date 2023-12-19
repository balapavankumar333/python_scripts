from collections import Counter

def extract_elements_with_frequency(lst, k):
    # Count the occurrences of each element
    element_counts = Counter(lst)

    # Extract elements with frequency greater than k
    result = [element for element, count in element_counts.items() if count > k]

    return result


my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
threshold = 1
result_list = extract_elements_with_frequency(my_list, threshold)

print(f"Elements with frequency greater than {threshold}: {result_list}")