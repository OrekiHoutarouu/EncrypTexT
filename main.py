from modules import encrypt, decrypt, utilities
import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title("EncrypTexT")
app.geometry("300x300")

main_menu_label = customtkinter.CTkLabel(app, text="Main Menu")
main_menu_label.pack(pady=10)

binary_option_button = customtkinter.CTkButton(app, text="Binary")
binary_option_button.pack(pady=5)

hexadecimal_option_button = customtkinter.CTkButton(app, text="Hexadecimal")
hexadecimal_option_button.pack(pady=5)

zenit_polar_option_button = customtkinter.CTkButton(app, text="ZENIT POLAR")
zenit_polar_option_button.pack(pady=5)

app.mainloop()