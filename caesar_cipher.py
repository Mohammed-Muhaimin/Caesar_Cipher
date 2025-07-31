

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    elif encode_or_decode != "encode":
        print("Invalid direction. Please use 'encode' or 'decode'.")
        return

    shift_amount = shift_amount % len(alphabet)  # Handle large shifts

    for letter in original_text:
        if letter.lower() not in alphabet:
            output_text += letter
        else:
            # Preserve original case
            is_upper = letter.isupper()
            letter_lower = letter.lower()

            shifted_position = alphabet.index(letter_lower) + shift_amount
            shifted_position %= len(alphabet)
            new_letter = alphabet[shifted_position]

            output_text += new_letter.upper() if is_upper else new_letter

    print(f"\nHere is the {encode_or_decode}d result: {output_text}\n")

def get_valid_shift():
    while True:
        try:
            shift = int(input("Type the shift number (0-25 recommended): "))
            return shift
        except ValueError:
            print("Please enter a valid integer.")

def main():
    to_continue = True
    print("Welcome to the Caesar Cipher Program!")

    while to_continue:
        print("\n" + "="*40)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ['encode', 'decode']:
            print("Invalid choice. Please try again.")
            continue

        text = input("Type your message:\n")
        shift = get_valid_shift()

        caesar(text, shift, direction)

        restart = input("\nType 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
        if restart != 'yes':
            to_continue = False
            print("\nThank you for using the Caesar Cipher Program!")

if __name__ == "__main__":
    main()
