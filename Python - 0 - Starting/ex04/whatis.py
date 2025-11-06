import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        if not argument.lstrip('-').isdigit():
            print("AssertionError: argument is not an integer")
        else:
            converted = int(argument)
            if converted % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    return

if __name__ == "__main__":
    main()
