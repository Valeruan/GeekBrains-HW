from sys import argv


def script_wage():
    hour, rate, prize = map(float, argv[1])
    print(f"{hour * rate + prize}")


script_wage()