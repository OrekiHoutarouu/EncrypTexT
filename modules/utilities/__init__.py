import customtkinter

def get_binary_encrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()
    
    if decrypted_text == None:
        return

    show_encrypted_or_decrypted_text("anything", "encrypted", "binary")


def get_binary_decrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text (1 byte each character)")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None:
        return
    
    while not validate_binary_encrypted_value(encrypted_text):
        dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type a valid binary code", entry_border_color="red")
        encrypted_text = dialogue.get_input()


    show_encrypted_or_decrypted_text("anything", "decrypted")


def get_hexadecimal_encrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    if decrypted_text == None:
        return

    show_encrypted_or_decrypted_text("anything", "encrypted", "hexadecimal")


def get_hexadecimal_decrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None:
        return

    show_encrypted_or_decrypted_text("anything", "decrypted")


def get_zenit_polar_encrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    if decrypted_text == None:
        return

    show_encrypted_or_decrypted_text("anything", "encrypted", "ZENIT POLAR")


def get_zenit_polar_decrypted_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    if encrypted_text == None:
        return

    show_encrypted_or_decrypted_text("anything", "decrypted")


def show_encrypted_or_decrypted_text(encrypted_or_decrypted_text, encrypted_or_decrypted, language="english"):
    new_window = customtkinter.CTkToplevel()
    new_window.geometry("350x425")

    textbox = customtkinter.CTkTextbox(new_window, width=300, height=400, corner_radius=20, fg_color="#2B2B2B")
    textbox.pack()

    textbox.insert("0.0", f"Here's your {encrypted_or_decrypted} text in {language}\n\n")
    textbox.insert("3.0", encrypted_or_decrypted_text)
    textbox.configure(state="disabled")


def validate_binary_encrypted_value(encrypted_binary_value):
    for character in encrypted_binary_value:
        if character == " ":
            character = "0"

        if not character.isnumeric():
            return False

        if int(character) < 0 or int(character) > 1:
            return False
    
    return encrypted_binary_value