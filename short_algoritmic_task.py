def print_three_digit_numbers():
    for number in range(100, 1000):
        if number % 7 == 0 or number % 9 == 0:
            print(number)


def main():
    print_three_digit_numbers()

if __name__ == '__main__':
    main()
