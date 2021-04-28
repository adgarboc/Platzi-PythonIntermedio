def run():
    # squares = []
    # for x in range(1,101):
    #     if x % 3 != 0:
    #         squares.append(x**2)

    #List comprehension:
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    squaresChallenge = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(f"squares challenge: {squaresChallenge}")

if __name__ == '__main__':
    run()