def capitalizeFirst1(arr):
    resultArr = []

    for strs in arr:
        resultArr.append(strs.capitalize())
    
    return(resultArr)



#with recurssion

def capitalizeFirst(arr):
    resultArr = []

    if len(arr) == 0:
        return resultArr

    resultArr.append(arr[0][0].upper() + arr[0][1:])

    return resultArr + capitalizeFirst(arr[1:])


print(capitalizeFirst(['taran', 'singh', 'mundhan']))