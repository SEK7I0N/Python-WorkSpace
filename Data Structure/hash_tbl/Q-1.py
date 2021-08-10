# return the first ṛepeating number in an array


inputA = [1, 2, 3, 4, 123, 5, 32, 3]
inputB = [1, 1, 2, 3, 4, 1, 5, 2, 3]
inputC = [1, 2, 3, 4, 5]


def return_first_repeating_number(arr):
    dict = {}
    for number in arr:
        if dict[number] == number:
            return number
        dict[number] = number
    return None


returned = return_first_repeating_number(inputA)

print(returned)
