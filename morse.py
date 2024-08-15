print( " welcome to my morse generator ")
result = input("entre the phrase you want to convert to morse code :")

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