from modules import decrypt, encrypt
from types import NoneType
import customtkinter

def get_binary_encrypted_value():
    """Gets the user's plain text and closes the tab if there is no input.
    If there is an input, the user's plain text get sent into the encrypt_decrypted_binary function.
    The encrypt_decrypted_binary function's return value get sent into the show_encrypted_or_decrypted_text function
    along with some data about the kind of encrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()
    
    if decrypted_text == None:
        return
    
    encrypted_text = encrypt.encrypt_decrypted_binary(decrypted_text)
    show_encrypted_or_decrypted_text(encrypted_text, "encrypted", "binary")


def get_binary_decrypted_value():
    """Gets the user's encrypted binary text, with 8 digits in each character. The tab closes if there is no input.
    If there is an input, the user's encrypted binary text get sent into the validate_binary_encrypted_value until a a non-false return value.
    The validate_binary_encrypted_value function's return value get sent into the decrypt_encrypted_binary function.
    The decrypt_encrypted_binary function's return value get sent into the show_encrypted_or_decrypted_text function 
    along with some data about the kind of decrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text (8 digits each character)")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None or encrypted_text == NoneType:
        return
    
    while not validate_binary_encrypted_value(encrypted_text):
        dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type a valid binary code", entry_border_color="red")
        encrypted_text = dialogue.get_input()

        if encrypted_text == None or encrypted_text == NoneType:
            return

    decrypted_text = decrypt.decrypt_encrypted_binary(encrypted_text)
    show_encrypted_or_decrypted_text(decrypted_text, "decrypted")


def get_octal_encrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()
    
    if decrypted_text == None:
        return
    
    encrypted_text = encrypt.encrypt_decrypted_octal(decrypted_text)
    show_encrypted_or_decrypted_text(encrypted_text, "encrypted", "octal")


def get_octal_decrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text (3 digits each character)")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None or encrypted_text == NoneType:
        return
    
    while not validate_octal_encrypted_value(encrypted_text):
        dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type a valid octal code", entry_border_color="red")
        encrypted_text = dialogue.get_input()

        if encrypted_text == None or encrypted_text == NoneType:
            return
    
    decrypted_text = decrypt.decrypt_encrypted_octal(encrypted_text)
    show_encrypted_or_decrypted_text(decrypted_text, "decrypted")


def get_hexadecimal_encrypted_value():
    """Gets the user's plain text and closes the tab if there is no input.
    If there is an input, the user's plain text get sent into the encrypt_decrypted_hexadecimal function.
    The encrypt_decrypted_hexadecimal function's return value get sent into the show_encrypted_or_decrypted_text function
    along with some data about the kind of encrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    if decrypted_text == None:
        return
    
    encrypted_text = encrypt.encrypt_decrypted_hexadecimal(decrypted_text)
    show_encrypted_or_decrypted_text(encrypted_text, "encrypted", "hexadecimal")


def get_hexadecimal_decrypted_value():
    """Gets the user's encrypted hexadecimal text, with 2 digits in each character. The tab closes if there is no input.
    If there is an input, the user's encrypted hexadecimal text get sent into the validate_hexadecimal_encrypted_value until a a non-false return value.
    The validate_hexadecimal_encrypted_value function's return value get sent into the decrypt_encrypted_hexadecimal function.
    The decrypt_encrypted_hexadecimal function's return value get sent into the show_encrypted_or_decrypted_text function 
    along with some data about the kind of decrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text (2 digits each character)")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None or encrypted_text == NoneType:
        return
    
    while not validate_hexadecimal_encrypted_value(encrypted_text):
        dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type a valid hexadecimal code", entry_border_color="red")
        encrypted_text = dialogue.get_input()

        if encrypted_text == None or encrypted_text == NoneType:
            return
        
    decrypted_text = decrypt.decrypt_encrypted_hexadecimal(encrypted_text)
    show_encrypted_or_decrypted_text(decrypted_text, "decrypted")


def get_zenit_polar_encrypted_value():
    """Gets the user's plain text and closes the tab if there is no input.
    If there is an input, the user's plain text get sent into the encrypt_decrypted_zenit_polar function.
    The encrypt_decrypted_zenit_polar function's return value get sent into the show_encrypted_or_decrypted_text function
    along with some data about the kind of encrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    if decrypted_text == None:
        return
    
    encrypted_text = encrypt.encrypt_decrypted_zenit_polar(decrypted_text)
    show_encrypted_or_decrypted_text(encrypted_text, "encrypted", "ZENIT POLAR")


def get_zenit_polar_decrypted_value():
    """Gets the user's plain text and closes the tab if there is no input.
    If there is an input, the user's plain text get sent into the decrypt_encrypted_zenit_polar function.
    The decrypt_encrypted_zenit_polar function's return value get sent into the show_encrypted_or_decrypted_text function
    along with some data about the kind of decrypted text.
    """

    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None:
        return
    
    decrypted_text = decrypt.decrypt_encrypted_zenit_polar(encrypted_text)
    show_encrypted_or_decrypted_text(decrypted_text, "decrypted")


def show_encrypted_or_decrypted_text(encrypted_or_decrypted_text, encrypted_or_decrypted, language="your language"):
    """Creates a new window, with 350px width and 425px height.
    Creates a textbox inside the window, with 300px width and 400px height.
    Inserts text into the textbox, containing the given arguments. (The text cannot be edited)

    Args:
        encrypted_or_decrypted_text (string): Encrypted or decrypted text that will be shown.
        encrypted_or_decrypted (string): Text telling if the text is encrypted or decrypted.
        language (string, optional): Type of encrypted or decrypted text. Defaults to "your language".
    """

    new_window = customtkinter.CTkToplevel()
    new_window.geometry("350x425")

    textbox = customtkinter.CTkTextbox(new_window, width=300, height=400, corner_radius=20, fg_color="#2B2B2B")
    textbox.pack()

    textbox.insert("0.0", f"Here's your {encrypted_or_decrypted} text in {language}:\n\n")
    textbox.insert("3.0", encrypted_or_decrypted_text)
    textbox.configure(state="disabled")


def validate_binary_encrypted_value(encrypted_binary_value):
    """Validates if the user's input is a binary text by checking if every character is numeric and in between 0 or 1.
    If the user's input is not a binary text, the function returns false.
    Otherwise, it returns the validated text.

    Args:
        encrypted_binary_value (string): User's unvalidated binary text.

    Returns:
        string: Validated user's binary text.
    """

    for character in encrypted_binary_value:
        if character == " ":
            character = "0"

        if not character.isnumeric():
            return False

        if int(character) < 0 or int(character) > 1:
            return False
    
    return encrypted_binary_value


def validate_octal_encrypted_value(encrypted_octal_value):
    for character in encrypted_octal_value:
        if character == " ":
            character = "0"
        
        if not character.isnumeric():
            return False
        
        if int(character) < 0 or int(character) > 7:
            return False
        
    return encrypted_octal_value


def validate_hexadecimal_encrypted_value(encrypted_hexadecimal_value):
    """Validates if the user's input is a hexadecimal text by checking if every character is alphanumeric.
    If the character is numeric, checks if it's in between 0 and 9.
    If the character is literary, checks if it's in between "A" and "F" or in between "a" and "f". 
    If the user's input is not a hexadecimal text, the function returns false.
    Otherwise, the function returns the validated text.

    Args:
        encrypted_hexadecimal_value (string): User's unvalidated hexadecimal text.

    Returns:
        string: Validated user's binary text.
    """

    for character in encrypted_hexadecimal_value:
        if character == " ":
            character = "0"

        if not character.isalnum():
            return False
        
        elif character.isnumeric():
            if int(character) < 0 or int(character) > 9:
                return False
        
        elif character.isalpha():
            if (ord(character) < 65 or ord(character) > 70) and (ord(character) < 97 or ord(character) > 102):
                return False
    
    return encrypted_hexadecimal_value