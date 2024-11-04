no_of_test_cases = int(input())
output = []
for j in range(no_of_test_cases):
    len_of_array = int(input())
    arr = [int(x) for x in input("Enter elements separated by comma: ").split(",")]

    if len(arr) == len_of_array:
        ra_one = 0
        g_one = 0
        if j % 2 == 0: # for odd numbered test cases, ra_one starts
            for i in range(0, len(arr), 2):
                ra_one+=arr[i]
            for i in range(1, len(arr), 2):
                g_one+=arr[i]
        if j % 2 != 0: # fir even numbered test cases, g_one starts
            for i in range(0, len(arr), 2):
                g_one+=arr[i]
            for i in range(1, len(arr), 2):
                ra_one+=arr[i]

        # print(g_one)
        # print(ra_one)

        if g_one > ra_one:
            output.append("true")
        elif g_one < ra_one:
            output.append("false")

for i in range(no_of_test_cases):
    print(output[i])
