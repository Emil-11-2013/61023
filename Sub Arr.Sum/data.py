def subarraysum(arr, n, sum):
    
    for i in range(n):
        current_sum = arr[i]

        j = i + 1
        while j <= n:
            if current_sum == sum:
                print("Sum found between")
                print("indexes % d and % d"%( i, j-1))


                return 1
            
            if current_sum > sum or j == n:
                break

            current_sum = current_sum + arr[j]
            j += 1

    print("No sub array found")
    return 0


arr = [3,6,2,2,56,1,0,9]
n = len(arr)
sum = 10 
subarraysum(arr, n, sum)
