#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in January 2023
# A program that rounds off decimals depending on input


def round_a_decimal(decimal, number_of_rounds):
    # Rounds off a decimal by reference

    decimal[0] = decimal[0] * 10**number_of_rounds
    decimal[0] += 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / 10**number_of_rounds


def main():
    # Gets the number of decimals and prints the new number

    number_chosen = []

    try:
        temp_number_text = input("Enter a decimal number: ")
        temp_number_integer = float(temp_number_text)
        number_chosen.append(temp_number_integer)
        decimals_to_round_text = input("Enter the number of decimals to round off to: ")
        decimals_to_round_integer = int(decimals_to_round_text)
        round_a_decimal(number_chosen, decimals_to_round_integer)
        print("\nThe rounded decimal is {}".format(number_chosen[0]))
    except ValueError:
        print("\nThis is not valid input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
