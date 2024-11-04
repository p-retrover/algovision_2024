pin = input()
if len(pin) == 4:
    if pin == pin [1]*len(pin):
        print("weak")
    else:
        first_counter = 0
        second_counter = 0
        for i in range(0,2): # checks for cyclic and consequitive in first 3
            if (int(pin[i])+1)%10 == int(pin[i+1]):
                first_counter += 1
        for i in range(1,3): # checks for cyclic and consequitive in last 3
            if (int(pin[i])+1)%10 == int(pin[i+1]):
                second_counter += 1
        if first_counter == 2 or second_counter == 2:
            print("weak")
        else:
            print("strong")
