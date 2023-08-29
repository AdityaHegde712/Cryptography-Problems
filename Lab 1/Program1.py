letters = 'abcdefghijklmnopqrstuvwxyz' # Initializing letters set
a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # Initializing values of key a which have an inverse
a_values_inverse = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25] # Inverse values
b_values = list(range(1, 26)) # Possible key b values.

def encrypt(a, b):
    plain_text = input("Enter the plain text: \n")
    cipher_text = ''.join(
        [letters[j] for j in 
         [((letters.index(i)*a) + b) % 26
          for i in plain_text]]
    )
    print(f"Cipher Text: {cipher_text}")
    return None

def decrypt(a, b):
    cipher_text = input("Enter cipher text: \n")
    a_inv = a_values_inverse[a_values.index(a)]
    # print(a_inv)
    plain_text = ''.join(
        [letters[j] for j in 
         [(a_inv * (letters.index(i) - b)) % 26
          for i in cipher_text]]
    )
    print(f"Plain Text: {plain_text}")
    return None

if __name__ == "__main__":
    a = int(input("Enter the first key (choose from: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25): \n"))
    b = int(input("Enter the second key (between 1 and 25): \n"))

    if not (a in a_values or b in b_values):
        print("Invalid key entered.")
        exit()
    choice = input("e to encrypt, d to decrypt: \n")
    if choice == 'e':
        encrypt(a, b)
    elif choice == 'd':
        decrypt(a, b)
    