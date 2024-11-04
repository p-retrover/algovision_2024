test_cases = int(input()) # no of test cases
given_numbers = []
for i in range(test_cases):
    given_number = int(input(""))
    given_numbers.append(given_number)

for i in range(test_cases):
    if given_numbers[i] % 7 == 0: # multiple of 7
        print("THALA FOR A REASON")
    else: # not a multiple of 7
        print("THALA FOR NO REASON")

