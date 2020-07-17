def isPrime(input_num):
    # All numbers greater than or equal to are not prime
    # 1 is neither prime nor composite
    # https://www.mathsisfun.com/prime-composite-number.html
    if input_num <= 1:
        return 0

    #2 is a prime number
    if input_num == 2:
        return 1

    #if a number has a factor D, it can be expressed as N = D * (N/D).
    #D or N/D has to be smaller or equal to Sqrt(N)
    upperLimit = int(input_num**0.5)

    #we iterate from 2 to SQRT(input_num) and check
    #for numbers less than input_num, if it is divisible by input_num
    #input_num % num<input_num would be zero, if these conditions are not 
    #satisfied the number is prime
    for i in range(2, upperLimit + 1):
        if i < input_num and input_num % i == 0:
            return 0
    return 1
