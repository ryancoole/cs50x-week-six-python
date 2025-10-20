# Prompt user for pyramid height between 1 and 8 inclusive
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        pass

# Build the pyramid
for i in range(1, height + 1):
    # Left spaces
    print(" " * (height - i), end="")
    # Left hashes
    print("#" * i, end="")
    # Gap
    print("  ", end="")
    # Right hashes
    print("#" * i)
