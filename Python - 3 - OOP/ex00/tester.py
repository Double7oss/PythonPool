from S1E9 import Character, Stark

def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    # This test should make an error to make sure that you have an abstract Class.
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()