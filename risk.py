from random import randint


def generate_random_numbers(num_of_rolls):
    random_rolls = []
    for roll in range(num_of_rolls):
        random_rolls.append(randint(1, 6))
    return sorted(random_rolls, reverse=True)


def numbers_to_print(random_rolls):
    numbers = str(random_rolls[0])
    if len(random_rolls) > 1:
        for i in range(1, len(random_rolls)):
            numbers = numbers + "-" + str(random_rolls[i])
    return numbers


def compare_results(attacker_rolls, defender_rolls):
    comparison_number = len(defender_rolls)
    attacker_loss = 0
    defender_loss = 0

    if len(attacker_rolls) < len(defender_rolls):
        comparison_number = len(attacker_rolls)

    for i in range(comparison_number):
        if attacker_rolls[i] > defender_rolls[i]:
            defender_loss += 1
        else:
            attacker_loss += 1
    return attacker_loss, defender_loss


def input_numbers_of_rolls():
    while True:
        try:
            rolls_attack = int(input("How many units attack: "))
            if rolls_attack in range(1, 4):
                break
        except ValueError:
            pass

    while True:
        try:
            rolls_defence = int(input("How many units defence: "))
            if rolls_defence in range(1, 3):
                break
        except ValueError:
            pass

    return(rolls_attack, rolls_defence)


def main():
    rolls_attack, rolls_defence = input_numbers_of_rolls()
    attacker = generate_random_numbers(rolls_attack)
    defender = generate_random_numbers(rolls_defence)

    attacker_loss, defender_loss = compare_results(attacker, defender)

    print("Dice:")
    print(("  Attacker: {}".format(numbers_to_print(attacker))))
    print(("  Defender: {}".format(numbers_to_print(defender))))
    print("\nOutcome: ")
    print("  Attacker: Lost {} units".format(attacker_loss))
    print("  Defender: Lost {} units".format(defender_loss))


main()
