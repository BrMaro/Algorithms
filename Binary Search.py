def binsearch(arr, target, start, end):
    """
    :param target: the target number whose index we are looking for
    :param start: the start of the subarray we are checking
    :param end:  the end of the subarray we are checking
    :return:  returns the index of the value we are looking for
    """
    # Base case
    if start > end:
        return "Not Found"

    middle = (start + end) // 2

    # if middle is equal target return middle
    if arr[middle] == target:
        return middle

    # if target is greater than middle,change middle to be between
    if arr[target] > middle:
        binsearch(arr, target, start, middle - 1)
    if arr[target] < middle:
        binsearch(arr, middle + 1, end)


binsearch([])
