

def sum_of_differences(array):
    elements = len(array) - 1
    total = 0
    index = 0
    if len(array) == 0 or len(array) == 1:
        return 0
    else:
        array.sort(reverse=True)
        while index != elements:
            partial_sum = array[index] - array[index+1]
            total += partial_sum
            index += 1
        return total



