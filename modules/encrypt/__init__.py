def encrypt_decrypted_binary(decrypted_text):
    encrypted_text = []

    for character in decrypted_text:
        encrypted_text.append(f'{ord(character):08b}')
    
    return f"{' '.join(encrypted_text)}"


def encrypt_decrypted_hexadecimal(decrypted_text):
    encrypted_text = []

    for character in decrypted_text:
        encrypted_text.append(f'{ord(character):02x}')

    return f"{''.join(encrypted_text)}"


def encrypt_decrypted_zenit_polar(decrypted_text):
    encrypted_text = []
    
    for character in decrypted_text:
        match(character):
            case 'z':
                encrypted_text.append('p')
            case 'p':
                encrypted_text.append('z')
            case 'e':
                encrypted_text.append('o')
            case 'o':
                encrypted_text.append('e')
            case 'n':
                encrypted_text.append('l')
            case 'l':
                encrypted_text.append('n')
            case 'i':
                encrypted_text.append('a')
            case 'a':
                encrypted_text.append('i')
            case 't':
                encrypted_text.append('r')
            case 'r':
                encrypted_text.append('t')
            case 'Z':
                encrypted_text.append('P')
            case 'P':
                encrypted_text.append('Z')
            case 'E':
                encrypted_text.append('O')
            case 'O':
                encrypted_text.append('E')
            case 'N':
                encrypted_text.append('L')
            case 'L':
                encrypted_text.append('N')
            case 'I':
                encrypted_text.append('A')
            case 'A':
                encrypted_text.append('I')
            case 'T':
                encrypted_text.append('R')
            case 'R':
                encrypted_text.append('T')
            case _:
                encrypted_text.append(character)
                
    return f"{''.join(encrypted_text)}"