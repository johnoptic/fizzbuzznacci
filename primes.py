prime_list = []

def find_primes(input_num):
    for num in range(2, input_num + 1): # First variable running through 2 upto the input value. 
        is_prime = True  # Assume the number is prime until after condition check
        for factors in range(2, int(num**0.5) + 1):  # takes num and runs a loop for secondary variable factor, between a range of 2 and nums square root.
            if num % factors == 0:  # condition check to see if the num is divisible by any of the factors. If it is only div by itself and 1.
                is_prime = False
                print(num)
                break
        if is_prime:
            i_am_prime = f"{num} is a PRIME!"
            print(i_am_prime)
            prime_list.append(num)

find_primes(100)

print(prime_list) # prints just the primes