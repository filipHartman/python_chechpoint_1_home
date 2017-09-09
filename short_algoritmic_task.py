def print_three_digit_numbers():
    for number in range(100, 1000):
        if number % 7 == 0 or number % 9 == 0:
            print(number)


def compare_words(*word):
    index = 0
    max_lenght = 0
    for i in word:
        if max_lenght < len(i):
            max_lenght = len(i)
            index = word.index(i)
            print(max_lenght, "\n", index)

    print("\n", word, "\n")
    print ("The longest word: ", word[index])


def change_to_roman_number(arabic_number):
    roman_main_chars = {1: "I",
                        5: "V",
                        10: "X",
                        50: "L",
                        100: "C",
                        500: "D",
                        1000: "M"}

    number_of_digits = len(arabic_number)

    if number_of_digits == 1:
        roman_number = change_units_number(roman_main_chars, arabic_number[-1])

    elif number_of_digits == 2:
        roman_units = change_units_number(roman_main_chars, arabic_number[-1])
        roman_tens = change_tens_number(roman_main_chars, arabic_number[-2])
        roman_number = roman_tens + roman_units
    elif number_of_digits == 3:
        roman_units = change_units_number(roman_main_chars, arabic_number[-1])
        roman_tens = change_tens_number(roman_main_chars, arabic_number[-2])
        roman_hundreds = change_hundreds_number(roman_main_chars, arabic_number[-3])
        roman_number = roman_hundreds + roman_tens + roman_units

    return roman_number


def change_units_number(roman_main_chars, arabic_number):
    if int(arabic_number) < 4:
        return roman_main_chars[1] * int(arabic_number)
    elif int(arabic_number) in range(5, 9):
        return roman_main_chars[5] + (int(arabic_number)-5)*roman_main_chars[1]
    elif int(arabic_number) == 9:
        return roman_main_chars[1] + roman_main_chars[10]
    elif int(arabic_number) == 4:
        return roman_main_chars[1] + roman_main_chars[5]


def change_tens_number(roman_main_chars, arabic_number):
    if int(arabic_number) < 4:
        return roman_main_chars[10] * int(arabic_number)
    elif int(arabic_number) in range(5, 9):
        return roman_main_chars[50] + (int(arabic_number)-5)*roman_main_chars[10]
    elif int(arabic_number) == 9:
        return roman_main_chars[10] + roman_main_chars[100]
    elif int(arabic_number) == 4:
        return roman_main_chars[10] + roman_main_chars[50]


def change_hundreds_number(roman_main_chars, arabic_number):
    if int(arabic_number) < 4:
        return roman_main_chars[100] * int(arabic_number)
    elif int(arabic_number) in range(5, 9):
        return roman_main_chars[500] + (int(arabic_number)-5)*roman_main_chars[100]
    elif int(arabic_number) == 9:
        return roman_main_chars[100] + roman_main_chars[1000]
    elif int(arabic_number) == 4:
        return roman_main_chars[100] + roman_main_chars[500]


def main():
    # print_three_digit_numbers()
    # word1 = input("First word: ")
    # word2 = input("Second word: ")
    # word3 = input("Third word: ")
    # compare_words(word1, word2, word3)
    arabic_number = input("Enter arabic_number: ")
    print(change_to_roman_number(arabic_number))


main()
