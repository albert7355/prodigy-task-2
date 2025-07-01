from PIL import Image
import os

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    encrypted_path = "encrypted_" + os.path.basename(image_path)
    image.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    decrypted_path = "decrypted_" + os.path.basename(image_path)
    image.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    image_path = input("Enter image file path: ")
    if not os.path.exists(image_path):
        print("Image file not found.")
        return

    try:
        key = int(input("Enter encryption/decryption key (number): "))
    except ValueError:
        print("Key must be an integer.")
        return

    if choice == 'E':
        encrypt_image(image_path, key)
    else:
        decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
