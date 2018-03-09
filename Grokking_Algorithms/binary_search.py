from __future__ import print_function,division

def binary_search(lists, item):
    low = 0
    high = len(lists) - 1            # low and high keep track of which part of the list you’ll search in.
    
    while low <= high :             # While you haven’t narrowed it down to one element …
        mid = (low + high) // 2      # check the middle element.
        guess = lists[mid]
        
        if guess == item:            # Found the item.
            return mid
        if guess > item:             # The guess was too high.
            high = mid - 1
        else:                        # The guess was too low
            low = mid + 1
    return None                     # The item doesn’t exist


if __name__ == "__main__":
    
    my_list = [1, 3, 5, 6, 7, 9, 11]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, 5))
    print(binary_search(my_list, -1))