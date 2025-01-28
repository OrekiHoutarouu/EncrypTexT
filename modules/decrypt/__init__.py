def decrypt_encrypted_binary(encrypted_text):
    decrypted_text = []
    bytes = []
    byte = []
    counter = 0

    for character in encrypted_text:
        if character == ' ':
            character = ''
            counter -= 1

        byte.append(character)
        counter += 1

        if counter == 8:
            bytes.append(''.join(byte)[:])
            byte.clear()
            counter = 0
    
    for byte in bytes:
        byte = int(byte, 2)
        decrypted_text.append(chr(int(byte)))

    return f"{''.join(decrypted_text)}"


def decrypt_encrypted_hexadecimal(encrypted_text):
    decrypted = []
    bytes = []
    byte = []
    counter = 0

    for character in encrypted_text:
        if character == ' ':
            character = ''
            counter -= 1

        byte.append(character)
        counter += 1

        if counter == 2:
            bytes.append(''.join(byte)[:])
            byte.clear()
            counter = 0

    for byte in bytes:
        byte = int(byte, 16)
        decrypted.append(chr(int(byte)))

    return f"{''.join(decrypted)}"


def decrypt_encrypted_zenit_polar(encrypted_text):
    decrypted_text = []
    
    for character in encrypted_text:
        match(character):
            case 'z':
                decrypted_text.append('p')
            case 'p':
                decrypted_text.append('z')
            case 'e':
                decrypted_text.append('o')
            case 'o':
                decrypted_text.append('e')
            case 'n':
                decrypted_text.append('l')
            case 'l':
                decrypted_text.append('n')
            case 'i':
                decrypted_text.append('a')
            case 'a':
                decrypted_text.append('i')
            case 't':
                decrypted_text.append('r')
            case 'r':
                decrypted_text.append('t')
            case 'Z':
                decrypted_text.append('P')
            case 'P':
                decrypted_text.append('Z')
            case 'E':
                decrypted_text.append('O')
            case 'O':
                decrypted_text.append('E')
            case 'N':
                decrypted_text.append('L')
            case 'L':
                decrypted_text.append('N')
            case 'I':
                decrypted_text.append('A')
            case 'A':
                decrypted_text.append('I')
            case 'T':
                decrypted_text.append('R')
            case 'R':
                decrypted_text.append('T')
            case _:
                decrypted_text.append(character)
                
    return f"{''.join(decrypted_text)}"