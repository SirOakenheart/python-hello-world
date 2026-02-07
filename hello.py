from utils import add_numbers, build_message


def main():
    x = 5
    y = 7

    total = add_numbers(x, y)
    message = build_message("Edward", total)

    print(message)


if __name__ == "__main__":
    main()
