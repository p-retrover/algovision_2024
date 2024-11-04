a= int(input())
b= int(input())
k = 0
p = 0
counter = 0
# increase p and increase by b*(10**p) 
while (k <= b):
    if (k+ a*(10**p) <= b):
        k += a*(10**p)
        p += 1
        counter+=1
    else:
        break

# now keep p constant and increase by b*(10**p)
p = p-1
while (k <= b):
    if (k+ a*(10**p) <= b):
        k += a*(10**p)
        counter+=1
    else:
        break

# increase by 1
while (k< b):
    k+=1
    counter+=1
print(counter)
