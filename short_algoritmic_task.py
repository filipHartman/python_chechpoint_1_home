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

if __name__ == '__main__':
        # print_three_digit_numbers()

        word1 = input("First word: ")
        word2 = input("Second word: ")
        word3 = input("Third word: ")
        compare_words(word1, word2, word3)
