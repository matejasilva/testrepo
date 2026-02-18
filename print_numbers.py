try:
    n = int(input("Enter n: "))
    
    if n < 1:
        print("n must be >= 1")
    else:
        for i in range(1, n + 1):
            print(i)

except ValueError:
    print("Invalid input. Please enter an integer.")
