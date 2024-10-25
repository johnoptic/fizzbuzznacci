# Run a loop that checks for primes (can only be divided by 1 and itself)
# Print to console

def find_primes(input_num):
    i = 1
    while(i <= input_num):
        if i % i == 0: # Prints every number because it is dividing by itself and checking for remainder
            print(i)
        i+=1

find_primes(20)

# checking each integer 1, 2, 3, 4, 5, 6, 7, 8 etc

# pick non prime 4
# is 4 divided by 1 = 4. yes.     is 4 divided by 4. yes. 
# just asking these two questions alone is not enough.