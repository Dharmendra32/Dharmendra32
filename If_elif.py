for n in range(1, 101):
    if n%2 == 0:
        print("buzz")
    elif n%3 == 0:
        print("fizzbuzz")
    elif n%5 == 0:
        print(("buzzfizz"))
    else:
        print(n)