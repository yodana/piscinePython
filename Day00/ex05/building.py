"""This is the main file for the exercice 05 of Day00."""

import sys


def ft_building(text):
    """This is the function who displays the sums of few caracters"""
    s = 0
    sum_upper = [s + 1 for c in text if c.isupper()]
    print(sum_upper)
    print("The text contains " + str(len(text)) + " characters:")
    #print(str(sum_upper[0]) + "upper letters")

def main():
    """This is the main function who handle the errors and cal the building function"""
    try:
        msg_error = "AssertationError: "
        assert len(sys.argv) <= 2, msg_error + "more than one argument is provided"
    except AssertionError as msg:
            print(msg)
            sys.exit(1)
    ft_building(sys.argv[1])

if __name__ == "__main__":
    main()