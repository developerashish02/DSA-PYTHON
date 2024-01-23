

def removeDuplicate(arr):
    my_dict = {}
    result = []

    for ele in arr:
        # if this element is already present then continue not put again in map
        if ele in my_dict:
            continue

        my_dict[ele] = True
        result.append(ele)

    return result


arr = [1, 2, 3, 4, 5, 3, 2, 4]
res = removeDuplicate(arr)
print(res)
