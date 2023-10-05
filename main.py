class Colors:
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    END = "\033[0m"
print("********************************************************************************\n")
print(Colors.GREEN+Colors.BOLD+"This program uses the map key to decrypt the Monoalphabetic cipher text.\n"+Colors.END)
print("********************************************************************************\n")
#read from file
with open('Aleem S.txt', 'r', encoding='UTF-8') as file:
    cipher_text = file.read()

# Decrypting using map key
key = {
    'J': 'A',
    'V': 'B',
    'F': 'C',
    'I': 'D',
    'W': 'E',
    'T': 'F',
    'M': 'G',
    'Z': 'H',
    'X': 'I',
    'A': 'J',
    'E': 'K',
    'L': 'L',
    'Y': 'M',
    'O': 'N',
    'G': 'O',
    'K': 'P',
    'N': 'Q',
    'C': 'R',
    'D': 'S',
    'P': 'T',
    'U': 'U',
    'H': 'V',
    'B': 'W',
    'S': 'X',
    'R': 'Y',
    'Q': 'Z',
}

# Create a new file and write the plain text to it.
with open("plain_text.txt", 'w', encoding='UTF-8') as file:

    for char in cipher_text:
        file.write(key.get(char, char))
        print(key.get(char, char),end="")


