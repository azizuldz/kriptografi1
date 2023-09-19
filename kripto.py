def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Pilih tindakan (encrypt/decrypt): ").lower()
    if choice == "encrypt":
        text = input("Masukkan teks yang akan dienkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (angka): "))
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Teks terenkripsi:", encrypted_text)
    elif choice == "decrypt":
        encrypted_text = input("Masukkan teks yang akan didekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (angka): "))
        decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
        print("Teks terdekripsi:", decrypted_text)
    else:
        print("Pilihan tidak valid. Silakan pilih 'encrypt' atau 'decrypt'.")

if __name__ == "__main__":
    main()
