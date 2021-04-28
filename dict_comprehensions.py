from math import sqrt

def run():
    # dict = {}
    # for x in range(1,101):
    #     if x % 3 != 0:
    #         dict[x] = x**3

    dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict)

    dict_challenge = {i:sqrt(i) for i in range(1, 1001)}
    print(dict_challenge)

if __name__ == '__main__':
    run()