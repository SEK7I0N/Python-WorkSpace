def canBeIncreasing(nums):

    len_of_nums = len(nums)
    Flag = False
    index_i = 0
    while index_i < len_of_nums:
        lst = []
        index_j = 0
        while index_j < len_of_nums:
            if index_i != index_j:
                lst.append(nums[index_j])
            index_j += 1
        if all(i < j for i, j in zip(lst, lst[1:])):
            return True
        index_i += 1
    return False


nums = [1, 7, 8, 2, 8]


print(canBeIncreasing(nums))

res = all(i < j for i, j in zip(nums, nums[1:]))
# print(res)
