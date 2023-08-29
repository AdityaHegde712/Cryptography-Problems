# Addition and subtraction operations.
def addition_subtraction(Axb, Bxb):
    Cx = ""
    if Axb == Bxb:
        return "00000000"
    
    for i in range(7, -1, -1):
        if not Axb[i] == Bxb[i]:
            if 7-i == 0:
                Cx += " + 1"
            else:
                Cx += f" + x^{7-i}"
    return Cx[3:]

# Multiplication operation
def multiplication(Axb, Bxb):
    max_degree = 8
    modulo = [1, 0, 0, 0, 1, 1, 0, 1, 1]
    b_list1 = [int(i) for i in Axb]
    b_list2 = [int(i) for i in Bxb]
    print(b_list1, b_list2)

    # Polynomial multiplication
    product = [0] * (max_degree * 2 - 1)
    for i in range(max_degree):
        for j in range(max_degree):
            product[i + j] ^= b_list1[i] & b_list2[j]

    # Modulo reduction
    while len(product) >= max_degree:
        if product[0] == 1:
            for i in range(max_degree):
                product[i] ^= modulo[i]
        product.pop(0)

    result = []
    for i in range(len(product)):
        if product[i] == 1:
            exponent = len(product) - 1 - i
            if exponent == 0:
                result.append('1')
            elif exponent == 1:
                result.append('x')
            else:
                result.append(f'x^{exponent}')

    result = ' + '.join
    return result
    
# Intermediate function for polynomial to binary conversion.
def polyToBin(polynomial):
    binary = ""
    exponents_present = ""
    for i in polynomial:
        if i == 'x':
            exponents_present += '1'
        elif i.startswith('x'):
            exponents_present += i[-1] # Takes the exponent associated with the term
        elif i == '1':
            exponents_present += '0'
    
    # Now suppose I have exponents_present = 65310
    highest = int(exponents_present[0])
    lowest = int(exponents_present[-1])

    if highest > 7:
        print("Error: Exponent too high")
        exit()
    
    for i in range(highest, -1, -1):
        if str(i) in exponents_present:
            binary += '1'
        else:
            binary += '0'
    return binary

# Main function
if __name__ == "__main__":
    m = int(input("Enter a value for m: "))
    while True:
        choice = input("\n1. Addition/Subtraction \n2. Multiplication \n3. Exit\nEnter your choice: ")

        Ax = [i for i in input("\nEnter A(x) in polynomial form [x3 + x1 + 1]: ").split(' ') if not i == '+']
        Bx = [i for i in input("\nEnter B(x) in polynomial form [x3 + x1 + 1]: ").split(' ') if not i == '+']
        
        Axb = polyToBin(Ax).zfill(8)
        Bxb = polyToBin(Bx).zfill(8)

        print("\nA(x) in binary: ", Axb)
        print("\nB(x) in binary: ", Bxb, '\n')

        if choice == '1':
            print("\nA(x) + B(x) = ", addition_subtraction(Axb, Bxb))
        elif choice == '2':
            print("\nA(x) * B(x) = ", multiplication(Axb, Bxb))
        elif choice == '3':
            exit()
        else:
            print("Invalid choice")
    
    