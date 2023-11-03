
def selectionSort(array):

    for i in range(len(array)):
x        last = len(array) - 1 - i
        maxIndex = 0

        for j in range(1, last+1):
            # find max index
            if array[j] > array[maxIndex]:
                maxIndex = j

        # find max index the swap the elements
        array[last], array[maxIndex] = array[maxIndex], array[last]

    return array


array = [6, 5, 4, 3, 2, 1]
print(selectionSort(array))
