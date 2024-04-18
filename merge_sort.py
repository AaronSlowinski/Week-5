'''
Merge Sort Example
By: Jack Seymour
Date 4/30/2023
'''


def merge_sort(items: list) -> list:
    '''
    Takes an unsorted list of comparable object and returns a new sorted list
    '''
    _l = len(items)
    if _l <= 1:
        return items

    left_sorted = merge_sort(items[:_l//2])  # left split
    right_sorted = merge_sort(items[_l//2:])  # right split

    return merge(left_sorted, right_sorted)


def merge(left: list, right: list) -> list:
    '''
    Helper function - takes two comparible lists and merges them together, returning a new merged list.
    '''
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result


unordered_list = [356, 746, 264, 569, 949, 895, 125, 455, 787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534,
                  201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373, 860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
print(merge_sort(unordered_list))
