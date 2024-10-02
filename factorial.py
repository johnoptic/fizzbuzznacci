import random
n = random.randint(1, 16)
message = f"The randomly chosen number is {n}."

print(message)

def find_factorial(n):
    if n < 0:
        raise ValueError("Say no to negative numbers.")
    if n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    else:
        factorial = 1
        steps = []
        for i in range(n, 0, -1):
            factorial *= i
            steps.append(str(i))

        steps_display = " x ".join(steps)
        print(f"{n}! = {steps_display} = {factorial}")
        return factorial

print(find_factorial(n))