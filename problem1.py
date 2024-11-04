side_len = int(input())

no_of_spaces = int((side_len -2)/2) - 2
# print(no_of_spaces)

if side_len % 2 == 0 :

    print("NO")

elif side_len == 5 : # bug

    print("YES")

    # figure

    for i in range(1,side_len+1):
        if i == 1 or i == side_len or i == int(side_len/2)+1: # for 1st, middle and last line
            print(side_len*"*")
        else:
            print("* * *")

elif side_len % 2 != 0 :

    print("YES")

    # figure

    for i in range(1,side_len+1):
        if i == 1 or i == side_len or i == int(side_len/2)+1:
            print(side_len*"*")
        else:

            print("*", no_of_spaces*" ","*", no_of_spaces*" ", "*")

