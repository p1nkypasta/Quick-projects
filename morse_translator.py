letters_to_morse = {
    'a' : '.-',
    'A' : '.-',
    'b' : '-...',
    'B' : '-...',
    'c' : '-.-.',
    'C' : '-.-.',
    'd' : '-..',
    'D' : '-..',
    'e' : '.',
    'E' : '.',
    'f' : '..-.',
    'F' : '..-.',
    'g' : '--.',
    'G' : '--.',
    'h' : '....',
    'H' : '....',
    'i' : '..',
    'I' : '..',
    'j' : '.---',
    'J' : '.---',
    'k' : '-.-',
    'K' : '-.-',
    'l' : '.-..',
    'L' : '.-..',
    'm' : '--',
    'M' : '--',
    'n' : '-.',
    'N' : '-.',
    'o' : '---',
    'O' : '---',
    'p' : '.--.',
    'P' : '.--.',
    'q' : '--.-',
    'Q' : '--.-',
    'r' : '.-.',
    'R' : '.-.',
    's' : '...',
    'S' : '...',
    't' : '-',
    'T' : '-',
    'u' : '..-',
    'U' : '..-',
    'v' : '...-',
    'V' : '...-',
    'w' : '.--',
    'W' : '.--',
    'x' : '-..-',
    'X' : '-..-',
    'y' : '-.--',
    'Y' : '-.--',
    'z' : '--..',
    'Z' : '--..',
    ' ' : '/'
}

def morse_code(phrase):
    print('input something to translate')
    translation = ''
    for letter in phrase:
        translation += letters_to_morse[letter]
    print(translation)

morse_code(input('input phrase to translate --->'))
