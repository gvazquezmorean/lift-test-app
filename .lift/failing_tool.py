#!/usr/bin/env python3
import argparse

def emit_version():
    print("1")


def emit_name():
    print("failing_tool")


def emit_applicable():
    print("true")

def run():
    print('[{\"type\" : \"lift test\",\"message\" : \"testing lift\", \"file\" : \".lift/failing_tool.py\",\"line\" : 1}]')
    # raise Exception('Feeling under the weather')

def main():
    parser = argparse.ArgumentParser(description='Failing Tool')
    parser.add_argument('command', metavar='COMMAND', help='Command')

    args = parser.parse_args()

    command = args.command

    if command == "version":
        emit_version()
    elif command == "name":
        emit_name()
    elif command == "applicable":
        emit_applicable()
    elif command == "run":
        run()

if __name__ == "__main__":
    main()
