number = int(input())
print(number, end=' ')
while number != 1:
    if number % 2 == 0 : # if even divide it by 2
        print(int(number/2), end = ' ')
        number = int(number/2)
        continue
        
    elif number % 2 != 0 : # elif odd mutiply by 3 then add 1
        print((int(number*3)+1), end = ' ')
        number = int((number*3)+1)
        continue
