'''
Swopnil N. Shrestha
Sorting Problem
October 29, 2018
'''

def insertion_sort(li:list, show_steps:bool=False) -> list:

    for index in range(1,len(li)):
        current_value = li[index]
        position = index

        while position > 0 and li[position-1] > current_value:
            li[position] = li[position-1]
            position = position-1

        li[position] = current_value
        if show_steps == True: print(li)

    return li

def merge_sort(li:list, show_steps:bool=False) -> list:

    if show_steps == True: print("Splitting ",li)

    # Split into two left and right
    if len(li) > 1:
        mid = len(li) // 2
        left = li[:mid]
        right = li[mid:]

        merge_sort(left, show_steps)
        merge_sort(right, show_steps)

        i, j, k = 0,0,0

        # Compare and merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i = i + 1
            else:
                li[k] = right[j]
                j = j + 1
            k=k+1

        while i < len(left):
            li[k] = left[i]
            i= i + 1
            k= k + 1

        while j < len(right):
            li[k] = right[j]
            j= j + 1
            k= k + 1

    if show_steps == True: print("Merging ",li)

    return li



def main():
    li = [20, 16, 12, 14, 14, 15, 17, 17, 7, 13]
    
    # Sort without steps shown
    print(insertion_sort(li))
    print(merge_sort(li))

    # Sort with steps shown
    print("---Insertion Sort---")
    insertion_sort(li, show_steps=True)
    print("---Merge Sort---")
    merge_sort(li, show_steps=True)

if __name__=="__main__":
    main()