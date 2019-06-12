for A in range(1, 101):
    if A % 3 == 0 and A % 5 == 0:
        A = "FIZZBUZZ"
    elif A % 3 == 0:
        A = "FIZZ"
    elif A % 5 == 0:
        A = "BUZZ"
    print(A)
