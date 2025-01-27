from modules import encrypt, decrypt, utilities
import customtkinter 

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.title("EncrypTexT")
app.geometry("500x300")


tabview = customtkinter.CTkTabview(app, width=400, corner_radius=20)
tabview.pack()

tabview.add("Binary")
tabview.tab("Binary").grid_columnconfigure(0, weight=1)

tabview.add("Hexadecimal")
tabview.tab("Hexadecimal").grid_columnconfigure(0, weight=1)

tabview.add("ZENIT POLAR")
tabview.tab("ZENIT POLAR").grid_columnconfigure(0, weight=1)


binary_encrypt_button = customtkinter.CTkButton(tabview.tab("Binary"), text="Encrypt", command=utilities.get_binary_encrypt_value, corner_radius=10)
binary_encrypt_button.pack(pady=50)

binary_decrypt_button = customtkinter.CTkButton(tabview.tab("Binary"), text="Decrypt", command=utilities.get_binary_decrypt_value, corner_radius=10)
binary_decrypt_button.pack()

hexadecimal_encrypt_button = customtkinter.CTkButton(tabview.tab("Hexadecimal"), text="Encrypt", command=utilities.get_hexadecimal_encrypt_value, corner_radius=10)
hexadecimal_encrypt_button.pack(pady=50)

hexadecimal_decrypt_button = customtkinter.CTkButton(tabview.tab("Hexadecimal"), text="Decrypt", command=utilities.get_hexadecimal_decrypt_value, corner_radius=10)
hexadecimal_decrypt_button.pack()

zenit_polar_encrypt_button = customtkinter.CTkButton(tabview.tab("ZENIT POLAR"), text="Encrypt", command=utilities.get_zenit_polar_encrypt_value, corner_radius=10)
zenit_polar_encrypt_button.pack(pady=50)

zenit_polar_decrypt_button = customtkinter.CTkButton(tabview.tab("ZENIT POLAR"), text="Decrypt", command=utilities.get_zenit_polar_decrypt_value, corner_radius=10)
zenit_polar_decrypt_button.pack()


app.mainloop() 