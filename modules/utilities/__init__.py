import customtkinter

def get_binary_encrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "encrypted", "binary")


def get_binary_decrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "decrypted")


def get_hexadecimal_encrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "encrypted", "hexadecimal")


def get_hexadecimal_decrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "decrypted")


def get_zenit_polar_encrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your plain text")
    decrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "encrypted", "ZENIT POLAR")


def get_zenit_polar_decrypt_value():
    dialogue = customtkinter.CTkInputDialog(title="EncrypTexT", text="Type your encrypted text")
    encrypted_text = dialogue.get_input()

    show_encrypted_or_decrypted_text("anything", "decrypted")


def show_encrypted_or_decrypted_text(encrypted_or_decrypted_text, encrypted_or_decrypted, language="english"):
    new_window = customtkinter.CTkToplevel()
    new_window.geometry("350x400")

    textbox = customtkinter.CTkTextbox(new_window, width=300, height=400, corner_radius=20)
    textbox.pack()

    textbox.insert("0.0", f"Here's your {encrypted_or_decrypted} text in {language}\n\n")
    textbox.insert("3.0", encrypted_or_decrypted_text)
    textbox.configure(state="disabled")
