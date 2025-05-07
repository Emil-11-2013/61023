def equilibriumPoint(arr):
    leftsideSum = 0
    rightsideSum = 0
    n = len(arr)

    for i in range(n):
        leftsideSum = 0
        rightsideSum = 0

        for j in range(i):
            leftsideSum += arr[j]


            for j in range(i + 1, n):
                rightsideSum = 0



            if leftsideSum == rightsideSum:
                return i
    
    return -1

arr = [-4,6,2,0,0,1,1]
print("Element : ", arr[equilibriumPoint(arr)])
