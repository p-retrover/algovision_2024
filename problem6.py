arr = [int(x) for x in input("Enter elements separated by comma: ").split(",")]
for i in range(1, len(arr)): # i represents the difference between elements
    counter = 0
    for j in range(0, len(arr)-i): # j iterates over the array to find elements with diffence i
        if arr[j+i]==arr[j]:
            print(arr[j])
            counter+=1
        if counter != 0: # stops code from printing multiple elements with same difference
            break
    if counter != 0: # stops code from printing multiple elements of increasing difference
        break
