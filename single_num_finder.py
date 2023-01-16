#Given a non-empty array of integers, every element appears twice except for one.Find that single one.

# Solution using dictionary
def single_number(numbers: list):
    #empty dictionary to track occurences
    num_count_dict = {}
    for num in numbers:
        if num not in num_count_dict:
            num_count_dict[num] = 1
        else:
            num_count_dict[num] += 1
    for num, count in num_count_dict.items():
        # If a number has a count of 1, return it
        if count == 1:
            return num

# using xor operator
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res



test_list_1 = [0]
test_list_2 = [2, 2, 1]
test_list_3 = [1, 1, 2, 3, 3]
test_list_4 = [4, 1, 2, 1, 2]
test_list_5 = [2, 1, 4, 1, 2]

print(single_number(test_list_1))
print(single_number(test_list_2))
print(single_number(test_list_3))
print(single_number(test_list_4))
print(single_number(test_list_5))
print()
print(singleNumber(test_list_1))
print(singleNumber(test_list_2))
print(singleNumber(test_list_3))
print(singleNumber(test_list_4))
print(singleNumber(test_list_5))

