def isPrime(num):
    counter = 0
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            counter += 1
    if counter == 0: # prime
        return "prime"
    else: # not prime
        return "not prime"

no_of_cases = int(input())
numbers = []
for i in range(no_of_cases):
    number = int(input())
    numbers.append(number)
print("")
for i in range(no_of_cases):
    if isPrime(numbers[i]) == "not prime":
        print("NO")

    elif isPrime(numbers[i]) == "prime":
        ultimate_prime_counter = 0
        for j in range(2, int(numbers[i]/2)+2):
            # check if both of the numbers adding up to number are prime
            if (isPrime(j) == "prime" and isPrime(numbers[i] - j) == "prime"):
                ultimate_prime_counter += 1
        if ultimate_prime_counter == 0:
            print("NO")
        else:
            print("YES")

