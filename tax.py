#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 11, 2023
# This program asks the user for the area of an oval in cm. It then calculates.

import constants


def main():
    # get the subtotal
    subtotal = float(input("The subtotal is ($): "))
    # Calculate the tax and total
    tax = subtotal * constants.HST
    total = subtotal + tax
    print("")
    print("You entered a subtotal of ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()
