# Get number of roles for tree
tree_height = input("How tall is the height: ")
# convert to integer
tree_height = int(tree_height)

# Get the startiing spaces for the top tree
spaces = tree_height - 1

# there is one hash to start that will be incremented
hashes = 1

# Save stump spaces till later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while tree_height != 0:

    # Print the spaces
    for i in range(spaces):
        print(' ', end="")

        # print hashes
    for i in range(hashes):
        print('#', end="")

    print()

    spaces -= 1

    hashes += 2

    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end="")

print("#")
