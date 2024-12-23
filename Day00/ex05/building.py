"""This is the main file for the exercice 05 of Day00."""

import sys


def ft_building(text):
    """
    ft_building(text) -> None
    This is the function who displays the sums of few caracters"""
    sum_upper = sum(1 for c in text if c.isupper())
    print("The text contains " + str(len(text)) + " characters:")
    print(str(sum_upper) + " upper letters")
    sum_lower = sum(1 for c in text if c.islower())
    print(str(sum_lower) + " lower letters")
    sum_p = sum(1 for c in text if c in '!"#$%&\'()*+,-./:;<=>?@[]\\^_`{|}~')
    print(str(sum_p) + " punctuation marks")
    sum_space = sum(1 for c in text if c in " ")
    print(str(sum_space) + " spaces")
    sum_digit = sum(1 for c in text if c.isdigit())
    print(str(sum_digit) + " digit")


def main():
    """Main function who handle the errors and call the building function"""
    try:
        msg = "AssertationError: "
        assert len(sys.argv) <= 2, msg + "more than one argument is provided"
    except AssertionError as msg:
        print(msg)
        sys.exit(1)
    if len(sys.argv) == 2:
        ft_building(sys.argv[1])
    else:
        try:
            text = ""
            text = input("What is the text to count ?\n")
            ft_building(text + " ")
        except EOFError:
            ft_building(text)


if __name__ == "__main__":
    main()
