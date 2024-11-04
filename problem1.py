no_of_sides = int(input())
no_of_spaces = int((no_of_sides -2)/2) - 2
repeat = int((no_of_sides - 3)/2)
print(no_of_spaces)
if no_of_sides % 2 == 0 :
    print("NO")

elif no_of_sides == 5 : # bug
    print("YES")
    # figure
    print(no_of_sides*"*")

    for i in range(repeat):
        print("* * *")
    
    print(no_of_sides*"*")

    for i in range(repeat):
        print("* * *")

    print(no_of_sides*"*")

elif no_of_sides % 2 != 0 :
    print("YES")
    # figure
    print(no_of_sides*"*")

    for i in range(repeat):
        print("*", no_of_spaces*" ","*", no_of_spaces*" ", "*")

    print(no_of_sides*"*")

    for i in range(repeat):
        print("*", no_of_spaces*" ", "*", no_of_spaces*" ", "*")

    print(no_of_sides*"*")
