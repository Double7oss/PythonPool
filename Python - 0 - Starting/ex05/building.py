import sys
import string 

def main():
    
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    # if len(sys.argv) <= 2:
    #     len_arg = len(sys.argv[1])
    #     print(f"the text contains {len_arg}")
    if len(sys.argv) <= 2:
        count_upper = 0
        count_lower = 0
        count_digit = 0
        count_space = 0
        count_marks = 0
    if len(sys.argv) <= 1:
        argument = input("What is the text to count?\n")
    else:
        argument = sys.argv[1]
    print(argument)
    for ch in argument:
        if ch.isupper():
            count_upper += 1
        elif ch.islower():
            count_lower += 1
        elif ch.isspace():
            count_space += 1
        elif ch.isdigit():
            count_digit += 1
        elif ch in string.punctuation:
            count_marks += 1
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_marks} punctuation marks")
    print(f"{count_space} space")
    print(f"{count_digit} digits")



if __name__ == "__main__":
    main()
    
    