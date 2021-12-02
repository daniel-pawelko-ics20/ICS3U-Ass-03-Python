#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# Odd or even


def main():
    # main function for creating odd or even program

    # asking for input
    number = input("Enter an integer: ")
    number = int(number)

    # process/output
    if (number % 2) == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
