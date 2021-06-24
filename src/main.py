#!/usr/bin/python3.8
from Calculator import Calculator
import argparse


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("operation",
                        help="math operation to perform",
                        type=str)
    args = parser.parse_args()
    print(Calculator().resolve(args.operation))


