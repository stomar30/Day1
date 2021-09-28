#Python program to find common elements in three lists using sets.

def ios(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    
    set1 = s1.intersection(s2)
    res= set1.intersection(s3)
    
    final = list(res)
    
    print(final)

arr1 = [1, 5, 10, 20, 40, 80, 100]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
    
ios(arr1, arr2, arr3)
