alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input('type decode to encrypt and type encode to decrypt:\n')
text=input('ender your massage:\n').lower()
shift=int(input('how much shift:\n'))
def encrypt (plain_text, plain_shift):
    cipher_text=''
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position= position + plain_shift
        new_letter=alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)
encrypt(plain_text=text, plain_shift=shift)
