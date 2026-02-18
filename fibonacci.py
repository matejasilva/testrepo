try:
    n = int(input("Enter n: "))

    if n < 0:
        print("n must be >= 0")
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        print(a)

except ValueError:
    print("Invalid input. Please enter an integer.")
