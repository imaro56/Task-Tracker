import json
import sys

def operations(args):
    command = args[0]



if __name__ == '__main__':
    args = sys.argv[1:]
    print(args)
    if len(args) == 0:
        while True:
            string = input('Enter the command(help for details): ')
            operations(string.split())
    else:
        operations(args)