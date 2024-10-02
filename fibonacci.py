def print_fibonacci_up_to(num):
    a, b = 0, 1
    while a <= num:
        print(a, end=' ')
        a, b = b, a + b
    print()

print_fibonacci_up_to(20)
