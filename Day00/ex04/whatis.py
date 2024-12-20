import sys
import argparse

try:
    msg_error = "AssertationError: "
    assert len(sys.argv) == 2, msg_error + "more than one argument is provided"
    assert sys.argv[1].replace('-','',1).isdigit(), msg_error + "argument is not an integer"
except AssertionError as msg:
        print(msg)
        sys.exit(1)

n = int(sys.argv[1])

if ((n % 2) == 0):
    print("I'm Even")
else:
    print("I'm Odd")