import sys
from heifer_generator import HeiferGenerator


# List all cows. Accepts list of cow objects.
def list_cows(cows):
    for cow in cows:
        print(cow.get_name())


# Find a specific cow. Accepts a string name and a list of cow objects
def find_cow(name, cows):

    # For each cow in the list
    for cow in cows:
        # If the name matches then return the cow
        print(f"name is {name}")
        print(f"cow.get_name is{cow.get_name()}")

        if name == cow.get_name():
            cow_index = HeiferGenerator.cowNames.index(name)
            cow.set_image(HeiferGenerator.cowImages[cow_index])
            return cow

    # Return None if no match was found
    return None



if __name__ == "__main__":
    cows = HeiferGenerator.get_cows()

    # TODO test for bad input
    # try:

    # Print the list of available cows
    # Usage: cowsay.py -l
    if sys.argv[1] == '-l':
        list_cows(cows)

        # Print a message using a specified cow
        # Usage: cowsay.py -n COW MESSAGE
    elif sys.argv[1] == '-n':

        # Get the specified cow
        # TODO throw an error if the cow isn't found
        # TODO Why is this sys.argv[2], not sys.argv[3]?
        cow = find_cow(sys.argv[2], cows)
        print("sys.argv[2] is", sys.argv[2])
        print("cow is", cow)
        print(cows)
        print(sys.argv[3:])
        print(cow.get_image())

    # Print a message with the default cow
    # Usage: cowsay.py MESSAGE
