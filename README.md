# Morse Code Generator

## Description

This Python script converts English letters into Morse code. It allows users to input a phrase and receive the corresponding Morse code output.

## Features

- Converts each English letter to its Morse code representation.
- Handles spaces by retaining them in the output.
- Displays an error message for characters that are not letters.

## How It Works

1. The script welcomes users to the Morse code generator.
2. It prompts the user to enter a phrase to be converted.
3. It uses a predefined dictionary to convert each letter into Morse code.
4. It prints the resulting Morse code or an error message for invalid characters.

## Usage

1. Run the script.
2. Enter the phrase you want to convert when prompted.
3. View the Morse code output.

## Example

```
plaintextCopy code
Welcome to my Morse generator
Enter the phrase you want to convert to Morse code: hello world

Morse code: .... . .-.. .-.. ---  .-- --- .-. .-.. -..

```

## Code

```python
pythonCopy code
print("Welcome to my Morse generator")
result = input("Enter the phrase you want to convert to Morse code: ")

morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}

result_in_morse = ''

for char in result:
    if char.lower() in morse_code_dict:
        result_in_morse += morse_code_dict[char.lower()] + ' '
    elif char == ' ':
        result_in_morse += ' '
    else:
        print(f"Character '{char}' is not a letter in English.")

print("Morse code:", result_in_morse)

```

## Notes

- The script currently only supports English letters and spaces.
- Characters outside the English alphabet will trigger an error messag
