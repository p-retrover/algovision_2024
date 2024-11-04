no_of_sides = int(input())
if no_of_sides % 2 == 0 & (no_of_sides<=25 | no_of_sides>=4) :
    print("NO")
elif no_of_sides == 5 :
    print("YES")
    # figure
    print(no_of_sides*"*")

    for i in range(int((no_of_sides-3)/2)):
        print("* * *")
    
    print(no_of_sides*"*")

    for i in range(int((no_of_sides-3)/2)):
        print("* * *")
    
    print(no_of_sides*"*")
elif no_of_sides % 2 != 0 & (no_of_sides<=25 | no_of_sides>=4):
    print("YES")
    # figure
    print(no_of_sides*"*")

    for i in range(int((no_of_sides-3)/2)):
        print("*", int(((no_of_sides-3)/2)-2)*" ","*", int(((no_of_sides-3)/2)-2)*" ", "*")
    
    print(no_of_sides*"*")

    for i in range(int((no_of_sides-3)/2)):
        print("*", int(((no_of_sides-3)/2)-2)*" ", "*", int(((no_of_sides-3)/2)-2)*" ", "*")
    
    print(no_of_sides*"*")


