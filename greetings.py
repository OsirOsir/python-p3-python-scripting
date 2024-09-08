#!/usr/bin/env python3
import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = sys.argv[1]  # Accept input from the user
    greet(name)