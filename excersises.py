# pedac

# p - merge two arrays together in sorted order from greatest to least
# e -
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# nums3 = [3,4,5,6]
# nums4 = [1,2,12,20]
# output = [1,2,2,3,4,5,6,12,20]
#
# d - lists
# a - use one loop to check same indexes in both arrays and add indexes in greatest order to a new arrays

def mergeArrays (list1, m, list2, n):
    newList = []
    for i in range(0, max(n,m)):
        if list1[i] and list2[i]:
            if list1[i] < list2[i]:
                newList.append(list1[i])
                newList.append(list2[i])
            else:
                newList.append(list2[i])
                newList.append(list1[i])
        elif list1[i] and not list2[i]:
            newList.append(list1[i])
        else:
            newList.append(list2[i])
    return newList

print(mergeArrays([3,4,5,6], 4, [1,2,12,20], 4))
