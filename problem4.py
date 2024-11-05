pin = input()

def isWeak(num):
    if num == num [1]*len(num):
        return True
    else:
        first_counter = 0
        second_counter = 0
        for i in range(0,2): # checks for cyclic and consequitive in first 3 digits
            current_digit = int(num[i])
            next_digit = int(num[i+1])
            if (current_digit+1)%10 == next_digit:
                first_counter += 1
        for i in range(1,3): # checks for cyclic and consequitive in last 3 digits
            current_digit = int(num[i])
            next_digit = int(num[i+1])
            if (current_digit+1)%10 == next_digit:
                second_counter += 1
        if first_counter == 2 or second_counter == 2:
            return True
        else:
            return False

if len(pin) == 4:
    if isWeak(pin) == True:
        print("weak")
    else:
        print("strong")
