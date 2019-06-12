for A in range(1, 101):
    if A > 1:
        for i in range(2, A):
            if (A % i) == 0:
                break
        else:
            print(A)