# Piglatin encryption

def encrypt():
    piglatin = []
    sentence = input("Enter the normal sentence: \n").lower().split() # Initializing the sentence in usable format.
    for i in sentence:
        piglatin.append(str(i[1:] + i[0] + 'a'))
    piglatin = ' '.join(piglatin)
    print(f"Pig latin sentence: {piglatin}") # Printing the final sentence post pig-latin encryption

def decrypt():
    normal = []
    sentence = input("Enter the piglatin sentence: \n").lower().split()
    for i in sentence:
        j = i[:-1]
        normal.append(str(j[-1] + j[:-1]))
    normal = ' '.join(normal)
    print(f"Normal Sentence: {normal}")

if __name__ == "__main__":
    choice = input('e for encryption, d for decryption: \n')
    if choice == 'e':
        encrypt()
    elif choice == 'd':
        decrypt()
    else:
        exit()