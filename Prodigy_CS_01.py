small_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encryption(plain_text,shift_key):
    cipher_text=" "
    for char in plain_text:
        if char in small_letters:
            place=small_letters.index(char)
            new_place=(place+shift_key)%26
            encryptedchar=small_letters[new_place]
            cipher_text+=encryptedchar

        elif char in capital_letters:
            place=capital_letters.index(char)
            new_place=(place+shift_key)%26
            encryptedchar=capital_letters[new_place]
            cipher_text+=encryptedchar

        else:
            cipher_text += char

    print("-" * 30)
    print(f"Encrypted message:{cipher_text}")
    print("-" * 30)
    
def decryption(cipher_text,shift_key):
    plain_text=" "
    for char in cipher_text:
        if char in small_letters:
            place=small_letters.index(char)
            new_place=(place-shift_key)%26
            decryptedChar=small_letters[new_place]
            plain_text+=decryptedChar

        elif char in capital_letters:
            place=capital_letters.index(char)
            new_place=(place-shift_key)%26
            decryptedChar=capital_letters[new_place]
            plain_text+=decryptedChar

        else:
            plain_text += char

    print("-" * 30)
    print(f"Decrypted message:{plain_text}")
    print("-" * 30)

end=False

while not end:
    Question=input("What do you want to do:Encryption(e) or decryption(d)")
    Your_message=input("Enter you message:")
    key=int(input("Enter key:"))

    if Question=="e":
        encryption(plain_text=Your_message,shift_key=key)
    elif Question=="d":
        decryption(cipher_text=Your_message,shift_key=key)
    cipher_again=input("Do you want to keep encrypting and decrypting ?('yes' or 'no') ")
    if cipher_again=='no':
        end=True
        print("Exit")