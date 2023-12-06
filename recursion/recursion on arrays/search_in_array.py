
# return element is present or not in the array
def search_element(nums, target, index):
    # base case
    if index == len(arr):
        return False

    return arr[index] == target or search_element(nums, target, index + 1)


# return the index
def search_element_index(nums, target, index):
    # base case
    if index == len(arr):
        return -1

    if arr[index] == target:
        return index

    return search_element_index(nums, target, index + 1)


# iterating from last
def search_element_index_last(nums, target, index):
    # base case
    if index == -1:
        return -1

    if arr[index] == target:
        return index

    return search_element_index_last(nums, target, index - 1)


# return all the index

def search_element_all_index(nums, target, index, ans):
    # base case
    if index == len(nums):
        return ans

    # body of the functions
    if nums[index] == target:
        ans.append(index)

    return search_element_all_index(nums, target, index + 1, ans)

# search with without parameter of list


def search_element_all_index_2(nums, target, index):
    # create a list
    allAns = []
    # base case
    if index == len(nums):
        # allAns.append(index)
        return allAns

    if nums[index] == target:
        allAns.append(index)
    # recursion call
    ans = search_element_all_index_2(nums, target, index + 1)

    allAns = allAns + ans

    return allAns


# main
arr = [11, 22, 32, 1, 34, 1, 1]
target = 1
# ans = search_element(arr, target, 0)
# ans = search_element_index(arr, target, 0)
# ans = search_element_all_index(arr, target, 0, [])
ans = search_element_all_index_2(arr, target, 0)
print(ans)
