import re

def is_valid_vietnamese_phone(number):
    """
    Validate if the input number is a valid Vietnamese telephone number.

    Rules:
    - Vietnamese phone numbers typically start with 0.
    - Mobile numbers: 10 digits, starting with prefixes like 03, 05, 07, 08, or 09.
    - Landline numbers: 10 or 11 digits, starting with area codes like 02 (e.g., 028 for Ho Chi Minh City).

    Args:
        number (str): The phone number to validate.

    Returns:
        bool: True if the number is valid, False otherwise.
    """
    # Remove spaces and ensure it's a string
    number = str(number).replace(" ", "")

    # Define the regex pattern for Vietnamese phone numbers
    pattern = re.compile(r"^(0(3\d{8}|5\d{8}|7\d{8}|8\d{8}|9\d{8}|2\d{9,10}))$")

    return bool(pattern.match(number))

def main():
    print("Vietnamese Telephone Number Validator")
    print("Enter 'q' to quit.")

    while True:
        number = input("Enter a phone number: ")
        if number.lower() == 'q':
            print("Goodbye!")
            break

        if is_valid_vietnamese_phone(number):
            print(f"{number} is a valid Vietnamese phone number.")
        else:
            print(f"{number} is NOT a valid Vietnamese phone number.")

if __name__ == "__main__":
    main()
