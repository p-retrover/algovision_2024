no_of_sides = int(input())
no_of_spaces = int((no_of_sides -2)/2) - 2
repeat = int((no_of_sides - 3)/2)
# print(no_of_spaces)
if no_of_sides % 2 == 0 :
    print("NO")

elif no_of_sides == 5 : # bug
    print("YES")
    # figure
    for i in range(1,no_of_sides+1):
        if i == 1 or i == no_of_sides or i == int(no_of_sides/2)+1:
            print(no_of_sides*"*")
        else:
            print("* * *")

elif no_of_sides % 2 != 0 :
    print("YES")
    # figure
    for i in range(1,no_of_sides+1):
        if i == 1 or i == no_of_sides or i == int(no_of_sides/2)+1:
            print(no_of_sides*"*")
        else:
            print("*", no_of_spaces*" ","*", no_of_spaces*" ", "*")
