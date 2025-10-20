# Prompt user for credit card number
number = input("Number: ")

# Luhn’s Algorithm


def luhn_checksum(num):
    total = 0
    reverse_digits = num[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        # Double every second digit
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


# Validate number
if not number.isdigit():
    print("INVALID")
    exit()

# Checksum validation
if not luhn_checksum(number):
    print("INVALID")
    exit()

# Determine card type
length = len(number)
start_two = int(number[:2])
start_one = int(number[0])

if length == 15 and start_two in [34, 37]:
    print("AMEX")
elif length == 16 and 51 <= start_two <= 55:
    print("MASTERCARD")
elif start_one == 4 and length in [13, 16]:
    print("VISA")
else:
    print("INVALID")
