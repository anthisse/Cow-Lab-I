import sys
from heifer_generator import HeiferGenerator


# Throw an error if a cow wasn't found
class CowNotFoundError(Exception):
    pass


# List all cows. Accepts list of cow objects.
def list_cows(cows):
    print("Cows available: ")
    # For each cow in the list
    for cow in cows:
        # Print the name of the cow. End with a space.
        print(cow.get_name(), end=" ")


# Find a specific cow. Accepts a string name and a list of cow objects
def find_cow(name, cows):
    # For each cow in the list
    for cow in cows:
        # If the name is a cow name
        if name == cow.get_name():
            # Set the image of the cow using the index of the name of the cow
            cow.set_image(HeiferGenerator.cowImages[HeiferGenerator.cowNames.index(name)])
            # Return the cow
            return cow

    # Return None if no match was found
    return None


# Print a help message
# Usage: cowsay.py --help
def print_help_message():
    print("usage: cowsay.py [OPTION] MESSAGE")
    print("-l")
    print("\tList available cows")
    print()
    print("-n [COW] [MESSAGE]")
    print("\tSpecify a cow and a message")
    print()
    print("If no flag is specified, the message will be printed with the default cow.")


# Print a message
def print_message(cows):
    try:
        # Get the inputted cow image and print it
        cow = find_cow(sys.argv[2], cows)

        # Throw an error if a cow wasn't found
        if cow is None:
            raise CowNotFoundError

        # Print the message and speech bubble lines
        for i in sys.argv[3:]:
            print(i, end=" ")
        print()
        print(HeiferGenerator.quoteLines)
        print(cow.get_image())

    # Print that the requested cow wasn't found
    except CowNotFoundError:
        print(f"Could not find {sys.argv[2]} cow!")


# Print the default cow and a message
def print_default_cow(cows):
    # Print the message and speech bubble lines
    for i in sys.argv[1:]:
        print(i, end=" ")
    print()
    print(HeiferGenerator.quoteLines)
    # Print the default cow, which is the first entry in the heifer generator
    cows[0].set_image(HeiferGenerator.cowImages[0])
    print(cows[0].get_image())


def main():
    # Get a list of cows
    cows = HeiferGenerator.get_cows()

    try:
        # Print a help message
        if sys.argv[1] == '--help':
            print_help_message()

        # Print the list of available cows
        # Usage: cowsay.py -l
        elif sys.argv[1] == '-l':
            list_cows(cows)

        # Print a message using a specified cow
        # Usage: cowsay.py -n COW MESSAGE
        elif sys.argv[1] == '-n':
            print_message(cows)

        # Print a message with the default cow
        # Usage: cowsay.py MESSAGE
        # No flag was specified
        else:
            print_default_cow(cows)

    except IndexError:
        raise SystemExit("usage: cowsay.py [OPTION]\nTry 'cowsay.py --help' for more information.")


# Call main
if __name__ == "__main__":
    main()
