arr = [int(x) for x in input("Enter elements separated by comma: ").split(",")]

for i in range(1, len(arr)): # i represents the difference between elements
    for j in range(0, len(arr)-i): # j iterates over the array to see at which difference elements are same
        if arr[j+i]==arr[j]:
            print(i, arr[j])
        break # we are going from the lowest differences and least position elements so as soon as we get a twin pair, we can stop
