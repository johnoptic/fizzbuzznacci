def fizzbuzz(fizz, buzz):
    i=1
    while(i <= 101):
        if i % fizz == 0 and i % buzz == 0:
            print('FizzBuzz')
        elif i % fizz == 0:
            print('Fizz')
        elif i % buzz == 0:
            print('Buzz')

        else: print(i)
        i+=1


fizzbuzz(3,5)