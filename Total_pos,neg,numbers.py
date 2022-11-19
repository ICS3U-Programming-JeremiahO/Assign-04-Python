#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: November 13 2022
# This program asks the user to enter integers until the user wants to end (the user enters ‘q’ to quit). It then displays the total of positive numbers, negative numbers and zeros entered.


def main():

    # initialize variables
    # initializing counters
    p_num_counter = 0
    n_num_counter = 0
    z_counter = 0

    while True:
        # input
        # ask user for input
        User_input = input("Enter any number or press q to quit: ")
        # checks if user input is q
        if User_input == "q":
            print()
            print(
                "you have entered {} positive number(s), {} negative number(s), and {} zero(s).".format(
                    p_num_counter, n_num_counter, z_counter
                )
            )
            break
        # if user input is not q then convert user input to an integer
        else:
            try:
                User_number = int(User_input)
                # if user input is positive then the counter for positive numbers goes up by one
                if User_number != "q":
                    if User_number > 0:
                        # implementing counter
                        p_num_counter += 1
                # if user input is negative then the counter for negative numbers goes up by one
                if User_number < 0:
                    n_num_counter += 1
                # if user input is a zero then the counter for zeroes goes up by one
                if User_number == 0:
                    z_counter += 1
            # A try catch.
            # if user number does not equal q or an integer then it will say, " This is not an integer and loops back"
            except Exception:
                print()
                print("This is not an integer ")

    print()
    print("Thank you for playing ")


if __name__ == "__main__":
    main()
