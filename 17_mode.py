def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    dict_of_nums = {}

    for num in nums:
        if num in dict_of_nums:
            dict_of_nums[num] = dict_of_nums[num] + 1
        else:
            dict_of_nums[num] = 1

    max_count = max(dict_of_nums.values())

    max_value = [key for key in dict_of_nums if dict_of_nums[key]==max_count]

    return max_value[0]
