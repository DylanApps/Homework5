for A in range(1, 101):
    if A > 1:
        for i in range(2, A):
            if (A % i) == 0:
                if A % 3 == 0 and A % 5 == 0:
                    A = "FIZZBUZZ"
                elif A % 3 == 0:
                    A = "FIZZ"
                elif A % 5 == 0:
                    A = "BUZZ"
        else:
            A = "Prime"
    print(A)