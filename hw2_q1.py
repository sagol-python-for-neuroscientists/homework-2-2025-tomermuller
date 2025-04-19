MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }
DOT = '.'
PLUS = '+'
HYPEN = '-'
EQUAL = "="
TRANSLAT_SPECIAL_LETTER_DICT = {PLUS: MORSE_CODE.get(DOT), EQUAL: MORSE_CODE.get(HYPEN)}

def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    morse_code_text = ""

    with open(input_file, 'r') as input_text:
        english_text = input_text.read()
        morse_code_text = translate_text_to_morse_code(english_text)
        
    with open(output_file, 'w') as output_text:
        output_text.write(morse_code_text)


def translate_text_to_morse_code(input_text: str):
    """Input: String wrote in english, numbers and ".", ",", "'", "-", :" 
        Output: a translation on that string to morse code"""
    
    morse_code_text = input_text.upper()
    morse_code_text = morse_code_text.replace(" ", "\n")
    morse_code_text = morse_code_text.replace(DOT, PLUS)
    morse_code_text = morse_code_text.replace(HYPEN, EQUAL)

    for english_word, morse_word in MORSE_CODE.items():
        if english_word not in (DOT, HYPEN):
            morse_code_text = morse_code_text.replace(english_word, morse_word)
        
    for special_letter, morse_word in TRANSLAT_SPECIAL_LETTER_DICT.items():
        morse_code_text = morse_code_text.replace(special_letter, morse_word)

    return morse_code_text


if __name__ == "__main__":
    english_to_morse()
    print("Question 2 solution are found in file 'lorem_morse.txt'")