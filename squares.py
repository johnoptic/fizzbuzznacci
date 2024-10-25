def squares(num):
    return num * num

def sqrt(num):
    return num ** 0.5

def find_squares(input):
    for i in range(1, input):
        squares(i)
        sqrt(i)
        square_number = f"The square number of {i} is {squares(i)}"
        square_root = f"The square root of {i} is {sqrt(i)}"
        print(square_number)
        print(square_root)

find_squares(20)
        